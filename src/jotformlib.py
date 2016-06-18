from jotform import *
import os
import logging
import shelve

JOTFORM_API_KEY_ENVVAR = 'JOTFORM_API_KEY'
JOTFORM_API_BASE_URL = 'https://eu-api.jotform.com/'

DEFAULT_CACHE_FILENAME = "/tmp/jotform.cache"


class JotformClient:

    cache = None
    data_client = None

    def __init__(self, cache_filename=DEFAULT_CACHE_FILENAME, data_client=None):
        self.cache_filename = cache_filename
        self.cache = shelve.open(self.cache_filename)
        self.data_client = JotformAPIClient(os.environ[JOTFORM_API_KEY_ENVVAR], baseUrl=JOTFORM_API_BASE_URL)

    def _cache_store(self, key, data):
        """ Store data in the cache.
        """
        self.cache[key] = data
        return self.cache[key]

    def get_cached(self, cache_key, func):
        """ Get data from cache if fresh, otherwise from `func`.
        """
        logging.debug("Using cache")
        logging.debug("Cache keys: {}".format(self.cache.keys()))
        if cache_key in self.cache:
            logging.debug("Using cached data for key=\"{}\"".format(cache_key))
            return self.cache[cache_key]
        else:
            # return self._cache_store(cache_key, requests.get(url).json())
            return self._cache_store(cache_key, func)

    def get_submissions(self, use_cache=True):
        """ Get all submissions.
        """
        if use_cache is True:
            return self.get_cached(cache_key="submissions", func=self.data_client.get_submissions())
        else:
            return self.data_client.get_submissions()

    def get_forms(self, use_cache=True):
        """ Get all forms.
        """
        if use_cache is True:
            return self.get_cached(cache_key="forms", func=self.data_client.get_forms())
        else:
            return self.data_client.get_forms()

    def get_folders(self, use_cache=True):
        """ Get all folders.
        """
        if use_cache is True:
            return self.get_cached(cache_key="folders", func=self.data_client.get_folders())
        else:
            return self.data_client.get_folders()

    def find_folder(self, folder_name):

        def find_folder_inner(node):
            for f in node.get('subfolders', []):
                if f['name'] == folder_name:
                    return node
                else:
                    child = find_folder_inner(f)
                    if child is not None:
                        return child
            return None

        folders = self.get_folders()

        return find_folder_inner(folders['subfolders'])

class JotformDataClient:

    def __init__(self):
        pass

