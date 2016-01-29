import logging as log

class Language(object):
    def __init__(self, identifier, acronym, title):
        method_name = "Language"
        log.info('{}: initialization.'.format(method_name))
        self._id = identifier
        self._acronym = acronym
        self._title = title
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, identifier):
        self._id = identifier

    @property
    def acronym(self):
        return self._acronym
    @acronym.setter
    def acronym(self, acronym):
        self._acronym = acronym

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title

    def __str__(self):
        return 'Language: id={}, acronym={}, title={}'.format(self.id, self.acronym, self.title)