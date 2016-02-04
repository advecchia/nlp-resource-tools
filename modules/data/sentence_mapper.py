import logging as log
from common_mapper import CommonMapper
from modules.data.storage import Sentences
from src.storage.sentence import Sentence

class SentenceMapper(CommonMapper):
    def __init__(self):
        method_name = "SentenceMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))

    def insert(self, sentence_object):
        method_name = 'SentenceMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = Sentences.insert(paragraph_id=sentence_object.paragraph_id, 
                             number_of_words=sentence_object.number_of_words, 
                             order_in_paragraph=sentence_object.order_in_paragraph)
        sentence_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return sentence_object

    def update(self, sentence_object):
        method_name = 'SentenceMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = Sentences.update(paragraph_id=sentence_object.paragraph_id, 
                             number_of_words=sentence_object.number_of_words, 
                             order_in_paragraph=sentence_object.order_in_paragraph).where(Sentences.id==sentence_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, sentence_id):
        method_name = 'SentenceMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            sentence_object = Sentences.get(Sentences.id==sentence_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(sentence_object)
        except Exception as e:
            log.info('SentenceDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('SentenceDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self, paragraph_id):
        method_name = 'SentenceMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        sentences = []
        for db_sentence in Sentences.select().where(Sentences.paragraph_id==paragraph_id):
            sentences.append(self.mapper(db_sentence));
        log.info('{}: end.'.format(method_name))
        return sentences

    def mapper(self, db_sentence):
        method_name = 'SentenceMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return Sentence(identifier=db_sentence.id, paragraph_id=db_sentence.paragraph_id, 
                             number_of_words=db_sentence.number_of_words, 
                             order_in_paragraph=db_sentence.order_in_paragraph)