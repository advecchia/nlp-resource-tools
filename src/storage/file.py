import logging as log

class File(object):
    def __init__(self, id, parallel_file_id, name, size, modified, language):
        method_name = "File"
        log.info('{}: initialization.'.format(method_name))
        self._id = id
        self._parallel_file_id = parallel_file_id
        self._name = name
        self._size = size
        self._modified= modified
        self._language = language
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def parallel_file_id(self):
        return self._parallel_file_id
    @parallel_file_id.setter
    def parallel_file_id(self, parallel_file_id):
        self._parallel_file_id = parallel_file_id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size

    @property
    def modified(self):
        return self._modified
    @modified.setter
    def modified(self, modified):
        self._modified = modified

    @property
    def language(self):
        return self._language
    @language.setter
    def language(self, language):
        self._language = language