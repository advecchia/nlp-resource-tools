import logging as log

class Sentence(object):
    def __init__(self, id, paragraph_id, number_of_words, order_in_paragraph):
        method_name = "Sentence"
        log.info('{}: initialization.'.format(method_name))
        self._id = id
        self._paragraph_id = paragraph_id
        self._number_of_words = number_of_words
        self._order_in_paragraph = order_in_paragraph
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def paragraph_id(self):
        return self._paragraph_id
    @paragraph_id.setter
    def paragraph_id(self, paragraph_id):
        self._paragraph_id = paragraph_id

    @property
    def number_of_words(self):
        return self._number_of_words
    @number_of_words.setter
    def _number_of_words(self, number_of_words):
        self._number_of_words = number_of_words

    @property
    def order_in_paragraph(self):
        return self._order_in_paragraph
    @order_in_paragraph.setter
    def order_in_paragraph(self, order_in_paragraph):
        self._order_in_paragraph = order_in_paragraph