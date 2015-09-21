import logging as log

class Token(object):
    def __init__(self, id, sentence_id, token, lemma, pos, syllables, order_in_sentence, tf_idf, length, synonyms):
        method_name = "Token"
        log.info('{}: initialization.'.format(method_name))
        self._id = id
        self._sentence_id = sentence_id
        self._token = token
        self._lemma = lemma
        self._pos = pos
        self._syllables = syllables
        self._order_in_sentence = order_in_sentence
        self._tf_idf = tf_idf
        self._length = length
        self._synonyms = synonyms
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def sentence_id(self):
        return self._sentence_id
    @sentence_id.setter
    def sentence_id(self, sentence_id):
        self._sentence_id = sentence_id
        
    @property
    def token(self):
        return self._token
    @token.setter
    def token(self, token):
        self._token = token
        
    @property
    def lemma(self):
        return self._lemma
    @lemma.setter
    def lemma(self, lemma):
        self._lemma = lemma
        
    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, pos):
        self._pos = pos
        
    @property
    def syllables(self):
        return self._id
    @syllables.setter
    def syllables(self, syllables):
        self._syllables = syllables
        
    @property
    def order_in_sentence(self):
        return self._order_in_sentence
    @order_in_sentence.setter
    def order_in_sentence(self, order_in_sentence):
        self._order_in_sentence = order_in_sentence
        
    @property
    def tf_idf(self):
        return self._tf_idf
    @tf_idf.setter
    def tf_idf(self, tf_idf):
        self._tf_idf = tf_idf
        
    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, length):
        self._length = length
        
    @property
    def synonyms(self):
        return self._synonyms
    @synonyms.setter
    def synonyms(self, synonyms):
        self._synonyms = synonyms