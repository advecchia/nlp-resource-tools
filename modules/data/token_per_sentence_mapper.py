import logging as log
from common_mapper import CommonMapper
from modules.data.storage import TokensPerSentence
from src.storage.token_per_sentence import TokenPerSentence

class TokenPerSentenceMapper(CommonMapper):
    def __init__(self):
        method_name = "TokenPerSentenceMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))

    def insert(self, token_per_sentence_object):
        method_name = 'TokenPerSentenceMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = TokensPerSentence.insert(sentence_id=token_per_sentence_object.sentence_id, 
                             token_id=token_per_sentence_object.token_id,
                             order_in_sentence=token_per_sentence_object.order_in_sentence)
        token_per_sentence_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return token_per_sentence_object

    def update(self, token_per_sentence_object):
        method_name = 'TokenPerSentenceMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = TokensPerSentence.update(sentence_id=token_per_sentence_object.sentence_id,
                                         token_id=token_per_sentence_object.token_id,
                                         order_in_sentence=token_per_sentence_object.order_in_sentence).where(TokensPerSentence.id==token_per_sentence_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, token_per_sentence_id):
        method_name = 'TokenPerSentenceMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            token_per_sentence_object = TokensPerSentence.get(TokensPerSentence.id==token_per_sentence_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(token_per_sentence_object)
        except Exception as e:
            log.info('TokenDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('TokenDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self):
        method_name = 'TokenPerSentenceMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        tokens_per_sentence = []
        for db_token_per_sentence in TokensPerSentence.select():
            tokens_per_sentence.append(self.mapper(db_token_per_sentence));
        log.info('{}: end.'.format(method_name))
        return tokens_per_sentence

    def mapper(self, db_token_per_sentence):
        method_name = 'TokenPerSentenceMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return TokenPerSentence(identifier=db_token_per_sentence.id, 
                                sentence_id=db_token_per_sentence.sentence_id, 
                                token_id=db_token_per_sentence.token_id,
                                order_in_sentence=db_token_per_sentence.order_in_sentence)