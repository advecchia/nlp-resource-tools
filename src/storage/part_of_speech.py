import logging as log

class PartOfSpeech(object):
    def __init__(self, identifier, acronym, name, language_id):
        method_name = "PartOfSpeech"
        log.info('{}: initialization.'.format(method_name))
        self._id = identifier
        self._acronym = acronym
        self._name = name
        self._language_id = language_id
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
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def language_id(self):
        return self._language_id
    @language_id.setter
    def language_id(self, language_id):
        self._language_id = language_id

    def __str__(self):
        return 'PartOfSpeech: id={}, acronym={}, name={}, language_id={}'.format(self.id, self.acronym, self.name, self.language_id)