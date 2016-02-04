import logging as log

class PartOfSpeech(object):
    def __init__(self, identifier, tag, description, language_id):
        method_name = "PartOfSpeech"
        log.info('{}: initialization.'.format(method_name))
        self._id = identifier
        self._tag = tag
        self._description = description
        self._language_id = language_id
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, identifier):
        self._id = identifier

    @property
    def tag(self):
        return self._tag
    @tag.setter
    def tag(self, tag):
        self._tag = tag

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def language_id(self):
        return self._language_id
    @language_id.setter
    def language_id(self, language_id):
        self._language_id = language_id

    def __str__(self):
        return 'PartOfSpeech: id={}, tag={}, description={}, language_id={}'.format(self.id, self.tag, self.description, self.language_id)