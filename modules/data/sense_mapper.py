import logging as log
from common_mapper import CommonMapper
from modules.data.storage import Senses
from src.storage.sense import Sense

class SenseMapper(CommonMapper):
    def __init__(self):
        method_name = "SenseMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
    
    def insert(self, sense_object):
        method_name = 'SenseMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = Senses.insert(token_id=sense_object.token_id, 
                              related_token_id=sense_object.related_token_id,
                              sense_type=sense_object.sense_type, 
                              correlation=sense_object.correlation)
        query.execute()
        log.info('{}: end.'.format(method_name))
        return sense_object

    def update(self, sense_object):
        method_name = 'SenseMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = Senses.update(sense_type=sense_object.sense_type, 
                              correlation=sense_object.correlation).where(Senses.token_id==sense_object.token_id, 
                                                                          Senses.related_token_id==sense_object.related_token_id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, token_id, related_token_id):
        method_name = 'SenseMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            sense_object = Senses.get(Senses.token_id==token_id, Senses.related_token_id==related_token_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(sense_object)
        except Exception as e:
            log.info('SenseDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('SenseDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self):
        method_name = 'SenseMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        senses = []
        for db_sense in Senses.select():
            senses.append(self.mapper(db_sense));
        log.info('{}: end.'.format(method_name))
        return senses

    def mapper(self, db_sense):
        method_name = 'SenseMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return Sense(token_id=db_sense.token_id, 
                     related_token_id=db_sense.related_token_id, 
                     sense_type=db_sense.sense_type, 
                     correlation=db_sense.correlation)