import logging as log
from common_mapper import CommonMapper
from modules.data.storage import TokensPerFile
from src.storage.token_per_file import TokenPerFile

class TokenPerFileMapper(CommonMapper):
    def __init__(self):
        method_name = "TokenPerFileMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))

    def insert(self, token_per_file_object):
        method_name = 'TokenPerFileMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = TokensPerFile.insert(file_id=token_per_file_object.file_id, 
                             token_id=token_per_file_object.token_id,
                             count=token_per_file_object.count)
        query.execute()
        log.info('{}: end.'.format(method_name))
        return token_per_file_object

    def update(self, token_per_file_object):
        method_name = 'TokenPerFileMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = TokensPerFile.update(count=token_per_file_object.count).where(TokensPerFile.file_id==token_per_file_object.file_id, 
                                                                              TokensPerFile.token_id==token_per_file_object.token_id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, file_id, token_id):
        method_name = 'TokenPerFileMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            token_per_file_object = TokensPerFile.get(TokensPerFile.file_id==file_id, 
                                                      TokensPerFile.token_id==token_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(token_per_file_object)
        except Exception as e:
            log.info('TokenDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('TokenDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self, file_id):
        method_name = 'TokenPerFileMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        tokens_per_file = []
        for db_token_per_file in TokensPerFile.select().where(TokensPerFile.file_id==file_id):
            tokens_per_file.append(self.mapper(db_token_per_file));
        log.info('{}: end.'.format(method_name))
        return tokens_per_file

    def mapper(self, db_token_per_file):
        method_name = 'TokenPerFileMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return TokenPerFile(file_id=db_token_per_file.file_id, 
                            token_id=db_token_per_file.token_id,
                            count=db_token_per_file.count)