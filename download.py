from fabric.api import *
from jotform import *

import argparse
import os
import simplejson

JOTFORM_API_KEY_ENVVAR = 'JOTFORM_API_KEY'
JOTFORM_API_BASE_URL = 'https://eu-api.jotform.com/'

def download(folder_name='CIAFF2016_final'):
    """ Download all the data from all submissions"""
    print folder_name
    return {}

def _get_client():
    return JotformAPIClient(os.environ[JOTFORM_API_KEY_ENVVAR], baseUrl=JOTFORM_API_BASE_URL)


def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()
    download()

if __name__ == "__main__":
    main()