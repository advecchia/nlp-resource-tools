import logging as log
from common_mapper import CommonMapper
from modules.data.storage import Lemmas
from src.storage.lemma import Lemma

class LemmaMapper(CommonMapper):
    def __init__(self):
        method_name = 'LemmaMapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
    
    def insert(self, lemma_object):
        method_name = 'LemmaMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = Lemmas.insert(lemma=lemma_object.lemma, 
                             pos_id=lemma_object.pos_id, syllables=lemma_object.syllables, 
                             length=lemma_object.length)
        lemma_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return lemma_object

    def update(self, lemma_object):
        method_name = 'LemmaMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = Lemmas.update(lemma=lemma_object.lemma, 
                             pos_id=lemma_object.pos_id, syllables=lemma_object.syllables, 
                             length=lemma_object.length).where(Lemmas.id==lemma_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, lemma_id):
        method_name = 'LemmaMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            lemma_object = Lemmas.get(Lemmas.id==lemma_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(lemma_object)
        except Exception as e:
            log.info('LemmaDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('FilesDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self):
        method_name = 'LemmaMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        lemmas = []
        for db_lemma in Lemmas.select():
            lemmas.append(self.mapper(db_lemma));
        log.info('{}: end.'.format(method_name))
        return lemmas

    def mapper(self, db_lemma):
        method_name = 'LemmaMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return Lemma(identifier=db_lemma.id, lemma=db_lemma.lemma, 
                     pos_id=db_lemma.pos_id, syllables=db_lemma.syllables, 
                     length=db_lemma.length)