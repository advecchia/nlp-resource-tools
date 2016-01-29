import logging as log

class File(object):
    def __init__(self, identifier, parallel_file_id, name, size, modified, language_id):
        method_name = "File"
        log.info('{}: initialization.'.format(method_name))
        self._id = identifier
        self._parallel_file_id = parallel_file_id
        self._name = name
        self._size = size
        self._modified= modified
        self._language_id = language_id
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, identifier):
        self._id = identifier

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
    def language_id(self):
        return self._language_id
    @language_id.setter
    def language_id(self, language_id):
        self._language_id = language_id

    def __str__(self):
        return 'File: id={}, parallel_file_id={}, name={}, size={}, modified={}, language_id={}'.format(self.id, self.parallel_file_id, self.name, self.size, self.modified, self.language_id)
