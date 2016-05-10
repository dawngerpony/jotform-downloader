import os
import logging
import csv

import shutil
import sys
import time
from os.path import basename

import requests
import simplejson
from bs4 import BeautifulSoup
from fabric.api import task
from fabric.utils import puts, error
from fabric.utils import warn as fabric_warn
from jotform import *
from urlparse import urlparse

JOTFORM_API_KEY_ENVVAR = 'JOTFORM_API_KEY'
JOTFORM_API_BASE_URL = 'https://eu-api.jotform.com/'


def _get_client():
    return JotformAPIClient(os.environ[JOTFORM_API_KEY_ENVVAR], baseUrl=JOTFORM_API_BASE_URL)


# def main(debug=False):
#     client = _get_client()
#     # print_form_with_submissions(client, '61006200786346')
#     print_all_forms_and_submissions(debug)


# @task
# def print_all_forms_with_zero_submissions(folder_name='CIAFF2016_final'):
#     """ Print all forms that have had no submissions yet.
#     """
#     client = _get_client()
#     folders = client.get_folders()
#     folder = [f for f in folders['subfolders'] if f['name'] == folder_name][0]
#     forms = folder['forms']
#     print 'form_id,form_name,num_submissions'
#     for form in forms:
#         submissions = get_submissions(form)
#         if len(submissions) == 0:
#             print "{0},{1},{2}".format(form['id'], form['title'], len(submissions))


# @task
# def print_all_forms_and_number_of_submissions(debug=False):
#     """ Print all forms and associated submissions for that form.
#     """
#     client = _get_client()
#     forms = client.get_forms()
#     if debug:
#         print forms
#
#     for form in forms:
#         submissions = get_submissions(form)
#         if debug:
#             print_form_with_submissions(form['id'])
#         print "{0},{1},{2}".format(form['id'], form['title'], len(submissions))


@task
def print_form_with_submissions(form_id):
    """ Print data for a single form, along with all of the submissions
        for that form.
    """
    client = _get_client()
    form = client.get_form(form_id)
    submissions = get_submissions_for_form(form)
    print "Form:"
    print simplejson.dumps(form, indent=2)
    print "Submissions:"
    print simplejson.dumps(submissions, indent=2)


def get_submission_data_for_all_forms_in_folder(folder_name='CIAFF2016_final', client=None):
    if not client:
        client = _get_client()
    folders = client.get_folders()
    folder = [f for f in folders['subfolders'] if f['name'] == folder_name][0]
    forms = folder['forms']
    data = []
    for form in forms:
        submissions = get_submissions_for_form(form)
        data.append({'form': form, 'submissions': submissions})
    return data


def get_submissions_for_form(form, exclude_sample_submissions=True, client=None):
    if not client:
        client = _get_client()
    form_id = form['id']
    submissions = client.get_form_submissions(form_id)
    if exclude_sample_submissions:
        return [s for s in submissions if s['id'] != '#SampleSubmissionID']
    else:
        return submissions


@task
def download_all_data(folder='CIAFF2016_final', debug=False):
    forms_and_submissions = get_submission_data_for_all_forms_in_folder(folder)
    timestamp = int(time.time())
    with open('all_data-{}.json'.format(timestamp), 'w') as f:
        simplejson.dump(forms_and_submissions, f)
        print "Data written to {}".format(f.name)


@task
def print_submissions_as_csv(filename='all_data.json', debug=False, download_files=True):
    """ Takes submissions data from JotForm API and converts it to CSV.
    """
    if debug:
        puts("debug={}, download_files={}".format(debug, download_files))
    with open(filename) as f:
        submissions_response_object = simplejson.load(f)
    execution_id = int(time.time())
    form_ids = list(set([s['form_id'] for s in submissions_response_object['content']]))
    for form_id in form_ids:
        submissions = [s for s in submissions_response_object['content'] if s['form_id'] == form_id]
        generate_csv_for_form(execution_id, form_id, submissions, download_files)
    log("{} CSV files written to disk".format(len(form_ids)))


def generate_csv_for_form(execution_id, form_id, submissions, download_files=True):
    (column_names, submissions) = rows_to_column_names(submissions)
    log("Generated column names", column_names)
    rows = []
    for s in submissions:
        # keys: ['status', 'form_id', 'ip', 'created_at', 'updated_at', 'answers', 'flag', 'new', 'id']
        rows.append(answers_as_dict(s, execution_id, download_files))
    output_filename = "output-{}-{}.csv".format(execution_id, form_id)
    # print simplejson.dumps(rows, indent=2)
    with open(output_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(rows)
    log("{} rows written to disk. Filename=\"{}\"".format(len(rows), output_filename))

def answers_as_dict(submission, execution_id=None, download_files=True):
    """ 72 = photo

    """
    if not execution_id:
        execution_id = int(time.time())
    answers_in_order = [56, 42, 43, 60, 61, 53, 52, 26, 27, 20, 21, 22, 23, 47, 45, 28, 29, 41, 3, 4, 7, 6, 8, 77, 76,
                        75, 74, 73, 72, 58, 10, 12, 59, 14, 17, 16, 19, 18, 31, 30, 36, 35, 34, 33, 54, 57]
    excludes = [str(a) for a in []]
    answers = submission['answers']
    answers_as_text = {}
    for k in [str(a) for a in answers_in_order]:
        if k in answers and 'answer' in answers[k] and k not in excludes:
            answers_as_text[k] = extract_answer(int(k), answers[k], execution_id, download_files)
    return answers_as_text


def extract_answer(key, answer, execution_id, download_files=True):
    """ Print a single answer as CSV, or download the file if it's a URL.
    :param key:
    :param answer:
    :param execution_id:
    :return:
    """
    s = ""
    try:
        if 'type' not in answer and 'answer' in answer:
            s = unicode(answer['answer']).encode('utf8')
        elif 'type' in answer and 'answer' in answer:
            if answer['type'] == 'control_checkbox':
                s = '.'.join(answer['answer'])
            elif answer['type'] == 'control_fileupload':
                if len(answer['answer']) > 0 and download_files is True:
                    url = answer['answer'][0]
                    puts("Downloading file, url={}".format(url))
                    s = download_file(answer['answer'][0], execution_id)
                else:
                    s = ""
            elif answer['type'] == 'control_textarea' or answer['type'] == 'control_textbox':
                s = unicode(answer['answer']).encode('utf8')
            elif answer['type'] == 'control_time':
                s = "{}:{}".format(answer['answer']['hourSelect'], answer['answer']['minuteSelect'])
            elif answer['type'] == 'control_datetime':
                s = simplejson.dumps(answer['answer'])
            elif answer['type'] == 'control_email':
                s = simplejson.dumps(answer['answer'])
            elif answer['type'] == 'control_fullname':
                s = simplejson.dumps(answer['answer'])
            elif answer['type'] == 'control_radio':
                s = simplejson.dumps(answer['answer'])
            elif answer['type'] == 'control_birthdate':
                s = simplejson.dumps(answer['answer'])
            elif answer['type'] == 'control_spinner':
                s = simplejson.dumps(answer['answer'])
            else:
                warn("New answer type found: \"{}\"".format(answer['type']))
                s = unicode(answer['answer']).encode('utf8')
        else:
            warn("Nothing to print")
    except KeyError as e:
        error("KeyError: message=\"{}\", key={}, answer=\"{}\"".format(e.message, key, answer))
    except TypeError as e:
        error("TypeError: message=\"{}\", key={}, answer=\"{}\"".format(e.message, key, answer))
    except IndexError as e:
        error("IndexError: message=\"{}\", key={}, answer=\"{}\"".format(e.message, key, answer))
    return s


def download_file(url, execution_id):
    """ Download a file from a URL using the requests module, and save it to disk in a folder.
    """
    folder = "files-{}".format(execution_id)
    if not os.path.isdir(folder):
        os.makedirs(folder)
    o = urlparse(url)
    filename = "{}/{}".format(folder, basename(o.path))
    puts("url={}, path={}, filename={}, folder={}".format(url, o.path, filename, folder))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    puts("File saved to disk. filename=\"{}\"".format(filename))
    return filename


def rows_to_column_names(submissions):
    """ Retrieve column headings.
    """
    column_names = []
    all_answer_ids = [s['answers'].keys() for s in submissions]
    if len(all_answer_ids) != 1:
        print simplejson.dumps(all_answer_ids)
    else:
        return all_answer_ids[0], submissions
    # all_answer_ids = list(set([s['answers'].keys() for s in submissions]))
    log(simplejson.dumps(all_answer_ids))
    for a in [str(a) for a in all_answer_ids]:
        # log("Processing a={}".format(a))
        answer_texts = get_answer_text(a, submissions)
        sample_submissions = submissions_with_this_answer(a, submissions)
        answers = [s['answers'][a].get('answer', 'NO ANSWER') for s in sample_submissions]
        if len(answers) != len(sample_submissions):
            warn("{} of the sample submissions for answer_id={} do not have answers".format(len(sample_submissions) - len(answers), a))
        sample_submission = sample_submissions[0]
        if 'answer' not in sample_submission['answers'][a]:
            warn("Sample submission for answer_id={} is missing an answer".format(a))
        # text = sample_submission['answers'][a].get('text', "NO TEXT")
        # soup = BeautifulSoup(text, "html.parser")
        # text = soup.get_text()
        column_names.append(a)  # TODO extract the actual text
    return column_names, submissions


def submissions_with_this_answer(a, submissions):
    s = [s for s in submissions if a in s['answers']]
    # log(a, {'len': len(s), 'type': str(type(s))})
    if len(s) < 1:
        warn("No submissions with this answer!", {'a': a})
    # log("Submissions with this answer: {}".format(len(s)))
    return s


def get_answer_text(answer_id, submissions):
    log("Checking answer_id={} for differences".format(answer_id))
    subs = submissions_with_this_answer(answer_id, submissions)
    if len(subs) == 0:
        return "NO TEXT"
    log("{} subs found".format(len(subs)))
    answer_texts = [s['answers'][answer_id].get('text', "NONE") for s in subs]
    if len(answer_texts) < 1:
        return "NO TEXT"
    if len(set(answer_texts)) > 1:
        warn("Text for answer_id={} is different!".format(answer_id), list(set(answer_texts)))
    return answer_texts[0]


def msg(message, data={}):
    if data:
        return "{} | {}".format(message, simplejson.dumps(data))
    else:
        return message


def log(message, data=None):
    puts(msg(message, data))


def warn(message, data=None):
    fabric_warn(msg(message, data))


def crash(message, data):
    error(msg(message, data))
