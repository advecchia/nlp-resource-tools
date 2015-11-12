"""
"""
import logging as log
import pickle
import json
from modules.data.storage import Files, Paragraphs, Sentences, Tokens, database
from src.storage.file import File
from src.storage.paragraph import Paragraph
from src.storage.sentence import Sentence
from src.storage.token import Token

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

    def save_json_to_file(self, data, filename):
        method_name = "DataPersistency.save_json_to_file"
        log.info('{}: initialization.'.format(method_name))
        with open(filename, 'wb') as o:
            o.write(self.encode_string_to_json(data))
            o.close()
        log.info('{}: end.'.format(method_name))

    def read_json_from_file(self, filename):
        method_name = "DataPersistency.read_json_from_file"
        log.info('{}: initialization.'.format(method_name))
        with open(filename, 'rb') as i:
            data = i.read()
            i.close()
        log.info('{}: end.'.format(method_name))
        return self.decode_string_from_json(data)

    def encode_string_to_json(self, data):
        method_name = "DataPersistency.encode_string_to_json"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return json.dumps(data)

    def decode_string_from_json(self, data):
        method_name = "DataPersistency.decode_string_from_json"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return json.loads(data)

    def encode_file_to_json_stream(self, filename):
        method_name = "DataPersistency.encode_file_to_json_stream"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return json.dump(filename)

    def decode_file_from_json_stream(self, filename):
        method_name = "DataPersistency.decode_file_from_json_stream"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return json.load(filename)
    
    def before_request_handler(self):
        method_name = "DataPersistency.before_request_handler"
        log.info('{}: initialization.'.format(method_name))
        if not self._connection:
            self._database.connect()
        log.info('{}: end.'.format(method_name))
    
    def after_request_handler(self):
        method_name = "DataPersistency.after_request_handler"
        log.info('{}: initialization.'.format(method_name))
        if self._connection:
            self._database.close()
        log.info('{}: end.'.format(method_name))

class FileMapper(object):
    def __init__(self):
        method_name = "FileMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
    
    def file_to_db_insert(self, file_object):
        method_name = "FileMapper.file_to_db_insert"
        log.info('{}: initialization.'.format(method_name))
        query = Files.insert(parallel_file=file_object.parallel_file.id, name=file_object.name, 
                             size=file_object.size, modified=file_object.modified, language=file_object.language)
        file_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return file_object

    def file_to_db_update(self, file_object):
        method_name = "FileMapper.file_to_db_update"
        log.info('{}: initialization.'.format(method_name))
        query = Files.update(parallel_file_id=file_object.parallel_file.id, name=file_object.name, 
                         size=file_object.size, modified=file_object.modified, language=file_object.language).where(id==file_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def db_to_file_get_files(self):
        method_name = "FileMapper.db_to_file_get_files"
        log.info('{}: initialization.'.format(method_name))
        files = []
        for db_file in Files.select():
            files.append(self.mapper_db_to_file(db_file));
        log.info('{}: end.'.format(method_name))
        return files

    def db_to_file_get_file(self, file_id):
        method_name = "FileMapper.db_to_file_get_file"
        log.info('{}: initialization.'.format(method_name))
        
        try:
            file_object = Files.get(Files.id==file_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper_db_to_file(file_object)
        except Exception as e:
            log.info('FilesDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('FilesDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def mapper_db_to_file(self, db_file):
        method_name = "FileMapper.mapper_db_to_file"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return File(id=db_file.id, parallel_file_id=db_file.parallel_file_id, name=db_file.name, 
                             size=db_file.size, modified=db_file.modified, language=db_file.language)

# TODO: implement the below classes
class ParagraphMapper(object):
    def __init__(self):
        method_name = "ParagraphMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))

class SentenceMapper(object):
    def __init__(self):
        method_name = "SentenceMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))

class TokenMapper(object):
    def __init__(self):
        method_name = "TokenMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
