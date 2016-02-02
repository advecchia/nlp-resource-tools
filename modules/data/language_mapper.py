import logging as log
from common_mapper import CommonMapper
from modules.data.storage import Languages
from src.storage.language import Language


class LanguageMapper(CommonMapper):
    def __init__(self):
        method_name = 'LanguageMapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
    
    def insert(self, language_object):
        method_name = 'LanguageMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = Languages.insert(acronym=language_object.acronym, 
                                 title=language_object.title)
        language_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return language_object

    def update(self, language_object):
        method_name = 'LanguageMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = Languages.update(acronym=language_object.acronym, 
                                 title=language_object.title).where(Languages.id==language_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, language_id):
        method_name = 'LanguageMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            language_object = Languages.get(Languages.id==language_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(language_object)
        except Exception as e:
            log.info('LanguagesDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('LanguagesDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self):
        method_name = 'LanguageMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        languages = []
        for db_language in Languages.select():
            languages.append(self.mapper(db_language));
        log.info('{}: end.'.format(method_name))
        return languages

    def mapper(self, db_language):
        method_name = 'LanguageMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return Language(identifier=db_language.id, acronym=db_language.acronym, 
                    title=db_language.title)