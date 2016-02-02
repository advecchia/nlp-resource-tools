import logging as log
from common_mapper import CommonMapper
from modules.data.storage import Tokens
from src.storage.token import Token

class TokenMapper(CommonMapper):
    def __init__(self):
        method_name = "TokenMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))

    def insert(self, token_object):
        method_name = 'TokenMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = Tokens.insert(token=token_object.token, 
                             lemma_id=token_object.lemma_id, 
                             pos_id=token_object.pos_id, 
                             syllables=token_object.syllables, 
                             length=token_object.length)
        token_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return token_object

    def update(self, token_object):
        method_name = 'TokenMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = Tokens.update(token=token_object.token, 
                             lemma_id=token_object.lemma_id, 
                             pos_id=token_object.pos_id, 
                             syllables=token_object.syllables, 
                             length=token_object.length).where(Tokens.id==token_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, token_id):
        method_name = 'TokenMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            token_object = Tokens.get(Tokens.id==token_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(token_object)
        except Exception as e:
            log.info('TokenDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('TokenDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self):
        method_name = 'TokenMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        tokens = []
        for db_token in Tokens.select():
            tokens.append(self.mapper(db_token));
        log.info('{}: end.'.format(method_name))
        return tokens

    def mapper(self, db_token):
        method_name = 'TokenMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return Token(identifier=db_token.id, token=db_token.token, 
                             lemma_id=db_token.lemma_id, 
                             pos_id=db_token.pos_id, 
                             syllables=db_token.syllables, 
                             length=db_token.length)