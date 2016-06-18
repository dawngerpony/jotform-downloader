import simplejson

REPORTS = [
    'print_zero_submissions',
    'print_all_submissions_to_json',
    'print_all_forms_to_json',
    'print_all_folders_to_json',
]


def report_print_zero_submissions(client, folder_name='CIAFF2016_final', config=None):
    submissions = client.get_submissions()
    folders = client.get_folders()
    folder = [f for f in folders['subfolders'] if f['name'] == folder_name][0]
    forms = folder['forms']
    print 'form_id,form_name,num_submissions'
    for form in forms:
        submissions = get_submissions(form)
        if len(submissions) == 0:
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

