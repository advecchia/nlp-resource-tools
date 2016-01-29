import logging as log

class TokenPerSentence(object):
    def __init__(self, identifier, sentence_id, token_id, order_in_sentence):
        method_name = "TokenPerSentence"
        log.info('{}: initialization.'.format(method_name))
        self._id = identifier
        self._sentence_id = sentence_id
        self._token_id = token_id
        self._order_in_sentence = order_in_sentence
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, identifier):
        self._id = identifier

    @property
    def sentence_id(self):
        return self._sentence_id
    @sentence_id.setter
    def sentence_id(self, sentence_id):
        self._sentence_id = sentence_id

    @property
    def token_id(self):
        return self._token_id
    @token_id.setter
    def token_id(self, token_id):
        self._token_id = token_id

    @property
    def order_in_sentence(self):
        return self._order_in_sentence
    @order_in_sentence.setter
    def order_in_sentence(self, order_in_sentence):
        self._order_in_sentence = order_in_sentence

    def __str__(self):
        return 'TokenPerSentence: id={}, sentence_id={}, token_id={}, order_in_sentence={}'.format(self.id, self.sentence_id, self.token_id, self.order_in_sentence)