import logging as log

class TokenPerFile(object):
    def __init__(self, file_id, token_id, count):
        method_name = "TokenPerFile"
        log.info('{}: initialization.'.format(method_name))
        self._file_id = file_id
        self._token_id = token_id
        self._count = count
        log.info('{}: end.'.format(method_name))

    @property
    def file_id(self):
        return self._file_id
    @file_id.setter
    def file_id(self, file_id):
        self._file_id = file_id

    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, count):
        self._count = count

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, identifier):
        self._id = identifier

    def __str__(self):
        return 'TokenPerFile: file_id={}, token_id={}, count={}'.format(self.file_id, self.token_id, self.count)