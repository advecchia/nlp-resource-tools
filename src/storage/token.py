import logging as log

class Token(object):
    def __init__(self, identifier, token, lemma_id, pos_id, syllables, length):
        method_name = "Token"
        log.info('{}: initialization.'.format(method_name))
        self._id = identifier
        self._token = token
        self._lemma_id = lemma_id
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
    def token(self):
        return self._token
    @token.setter
    def token(self, token):
        self._token = token
        
    @property
    def lemma_id(self):
        return self._lemma_id
    @lemma_id.setter
    def lemma_id(self, lemma_id):
        self._lemma_id = lemma_id
        
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
        return 'Token: id={}, token={}, lemma_id={}, pos_id={}, syllables={}, length={}'.format(self.id, self.token, self.lemma_id, self.pos_id, self.syllables, self.length)
