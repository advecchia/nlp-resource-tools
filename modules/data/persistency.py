"""
"""
import logging as log
import pickle
import json
from modules.data.storage import database

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