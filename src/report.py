import simplejson

REPORTS = [
    'print_zero_submissions',
    'print_all_submissions_to_json',
    'print_all_forms_to_json',
    'print_all_folders_to_json',
]


def report_print_zero_submissions(client, config=None):
    print_zero_submissions(client, config, folder_name='CIAFF2016_DJ')
    print_zero_submissions(client, config, folder_name='CIAFF2016_BAND')


def print_zero_submissions(client, config, folder_name):
    submissions = client.get_submissions()
    # print "Looking for folder_name={0}".format(folder_name)
    folder = client.find_folder(folder_name)
    # print simplejson.dumps(folder, indent=2)
    forms = folder['forms']
    # print "Forms: {}".format(simplejson.dumps(forms, indent=2))
    print 'form_id,form_name,num_submissions'
    for form in forms:
        # print form['last_submission']
        if form['last_submission'] is None:
            print "{0},{1},{2}".format(form['id'], form['title'], len(submissions))

    print ""
    print "Zero Submissions Report"
    print "======================="
    print ""
    print "There are {} submissions.".format(len(submissions))


def report_print_all_submissions_to_json(client, config=None):
    print simplejson.dumps(client.get_submissions(), indent=2)


def report_print_all_forms_to_json(client, config=None):
    print simplejson.dumps(client.get_forms(), indent=2)


def report_print_all_folders_to_json(client, config=None):
    print simplejson.dumps(client.get_folders(), indent=2)

