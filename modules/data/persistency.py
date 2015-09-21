"""
"""
import logging as log
import pickle
import json
from storage import Files, Paragraphs, Sentences, Tokens, database
from src.storage.file import File
from src.storage.paragraph import Paragraph
from src.storage.sentence import Sentence
from src.storage.token import Token
from zim.stores import files

class DataPersistency(object):
    def __init__(self):
        method_name = "DataPersistency"
        log.info('{}: initialization.'.format(method_name))
        self._database = database
        self._connection = self._database.get_conn()
        log.info('{}: end.'.format(method_name))

    def save_dump_to_file(self, data, filename):
        method_name = "DataPersistency.save_dump_to_file"
        log.info('{}: initialization.'.format(method_name))
        with open(filename, 'wb') as o:
            pickle.dump(data, o)
            o.close()
        log.info('{}: end.'.format(method_name))

    def read_dump_from_file(self, filename):
        method_name = "DataPersistency.read_dump_from_file"
        log.info('{}: initialization.'.format(method_name))
        with open(filename, 'rb') as i:
            dump = pickle.load(i)
            i.close()
        log.info('{}: end.'.format(method_name))
        return dump

    def save_json_to_file(self):
        pass
    def read_json_from_file(self):
        pass

    def encode_string_to_json(self, data):
        return json.dumps(data)

    def decode_string_from_json(self, data):
        return json.loads(data)

    def encode_file_to_json(self, filename):
        return json.dump(filename)

    def decode_file_from_json(self, filename):
        return json.load(filename)
    
    def before_request_handler(self):
        if not self._connection:
            self._database.connect()
    
    def after_request_handler(self):
        if self._connection:
            self._database.close()

class FileMapper(object):
    def __init__(self):
        method_name = "FileMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
    
    def file_to_db_insert(self, file):
        method_name = "FileMapper.file_to_db_insert"
        log.info('{}: initialization.'.format(method_name))
        query = Files.insert(parallel_file=file.parallel_file.id, name=file.name, 
                             size=file.size, modified=file.modified, language=file.language)
        file.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return file

    def file_to_db_update(self, file):
        method_name = "FileMapper.file_to_db_update"
        log.info('{}: initialization.'.format(method_name))
        query = Files.update(parallel_file=file.parallel_file.id, name=file.name, 
                             size=file.size, modified=file.modified, language=file.language).where(id==file.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() > 0: return True
        else: return False

    def db_to_file_get_files(self):
        method_name = "FileMapper.db_to_file_get_files"
        log.info('{}: initialization.'.format(method_name))
        files = []
        for file in Files.select():
            files.append(self.mapper_db_to_file(file));
        log.info('{}: end.'.format(method_name))
        return files

    def db_to_file_get_file(self, id):
        method_name = "FileMapper.db_to_file_get_file"
        log.info('{}: initialization.'.format(method_name))
        try:
            file = Files.get(Files.id==id)
            log.info('{}: end.'.format(method_name))
            return self.mapper_db_to_file(file)
        except FilesDoesNotExist as e:
            log.info('FilesDoesNotExist {}: {}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            
    def mapper_db_to_file(self, db_file):
        method_name = "FileMapper.mapper_db_to_file"
        log.info('{}: initialization.'.format(method_name))
        return File(id==db_file.id, parallel_file_id=db_file.parallel_file, name=db_file.name, 
                             size=db_file.size, modified=db_file.modified, language=db_file.language)
        log.info('{}: end.'.format(method_name))