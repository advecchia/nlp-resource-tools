import logging as log
from common_mapper import CommonMapper
from modules.data.storage import PartsOfSpeech
from src.storage.part_of_speech import PartOfSpeech

class PartOfSpeechMapper(CommonMapper):
    def __init__(self):
        method_name = "PartOfSpeechMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
    
    def insert(self, pos_object):
        method_name = 'PartOfSpeechMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = PartsOfSpeech.insert(tag=pos_object.tag, 
                             description=pos_object.description,
                             language_id=pos_object.language_id)
        pos_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return pos_object

    def update(self, pos_object):
        method_name = 'PartOfSpeechMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = PartsOfSpeech.update(tag=pos_object.tag, 
                             description=pos_object.description,
                             language_id=pos_object.language_id).where(PartsOfSpeech.id==pos_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, pos_id):
        method_name = 'PartOfSpeechMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            pos_object = PartsOfSpeech.get(PartsOfSpeech.id==pos_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(pos_object)
        except Exception as e:
            log.info('PartOfSpeechDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('PartOfSpeechDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self):
        method_name = 'PartOfSpeechMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        pos = []
        for db_pos in PartsOfSpeech.select():
            pos.append(self.mapper(db_pos));
        log.info('{}: end.'.format(method_name))
        return pos

    def mapper(self, db_pos):
        method_name = 'PartOfSpeechMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return PartOfSpeech(identifier=db_pos.id, tag=db_pos.tag, 
                             description=db_pos.description,
                             language_id=db_pos.language_id)