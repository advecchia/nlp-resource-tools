import logging as log
from common_mapper import CommonMapper
from modules.data.storage import Files
from src.storage.file import File
# If are problems with self reference for files see:
# http://docs.peewee-orm.com/en/latest/peewee/models.html#self-referential-foreign-keys
class FileMapper(CommonMapper):
    def __init__(self):
        method_name = 'FileMapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
    
    def insert(self, file_object):
        method_name = 'FileMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = Files.insert(parallel_file_id=file_object.parallel_file_id, 
                             name=file_object.name, size=file_object.size, 
                             modified=file_object.modified, 
                             language_id=file_object.language_id)
        file_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return file_object

    def update(self, file_object):
        method_name = 'FileMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = Files.update(parallel_file_id=file_object.parallel_file_id, 
                             name=file_object.name, size=file_object.size, 
                             modified=file_object.modified, 
                             language_id=file_object.language_id).where(Files.id==file_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, file_id):
        method_name = 'FileMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            file_object = Files.get(Files.id==file_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(file_object)
        except Exception as e:
            log.info('FileDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('FileDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self):
        method_name = 'FileMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        files = []
        for db_file in Files.select():
            files.append(self.mapper(db_file));
        log.info('{}: end.'.format(method_name))
        return files

    def mapper(self, db_file):
        method_name = 'FileMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return File(identifier=db_file.id, parallel_file_id=db_file.parallel_file_id, 
                    name=db_file.name, size=db_file.size, modified=db_file.modified, 
                    language_id=db_file.language_id)