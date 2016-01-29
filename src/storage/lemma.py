import logging as log

class Lemma(object):
    def __init__(self, identifier, lemma, pos_id, syllables, length):
        method_name = "Lemma"
        log.info('{}: initialization.'.format(method_name))
        self._id = identifier
        self._lemma = lemma
        self._pos_id = pos_id
        self._syllables = syllables
        self._length = length
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, identifier):
        self._id = identifier
        
    @property
    def lemma(self):
        return self._lemma
    @lemma.setter
    def lemma(self, lemma):
        self._lemma = lemma

    @property
    def pos_id(self):
        return self._pos_id
    @pos_id.setter
    def pos_id(self, pos_id):
        self._pos_id = pos_id
        
    @property
    def syllables(self):
        return self._syllables
    @syllables.setter
    def syllables(self, syllables):
        self._syllables = syllables

    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, length):
        self._length = length

    def __str__(self):
        return 'Lemma: id={}, lemma={}, pos_id={}, syllables={}, length={}'.format(self.id, self.lemma, self.pos_id, self.syllables, self.length)
