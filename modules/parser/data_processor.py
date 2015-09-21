"""
"""
import logging as log
import nltk
import time, datetime
import os
class RawDataProcessor(object):
    def __init__(self, file_handler):
        method_name = "RawDataProcessor"
        log.info('{}: initialization.'.format(method_name))
        self._file_handler = file_handler
        log.info('{}: end.'.format(method_name))
        
    def tokenize(self):
        method_name = "RawDataProcessor.tokenize"
        log.info('{}: initialization.'.format(method_name))
        with open(self._file_handler, 'r') as f:
            data = f.read()
            f.close
        log.info('{}: return.'.format(method_name))
        return nltk.word_tokenize(data)

    def tokenize_sentence(self, sentence):
        method_name = "RawDataProcessor.tokenize"
        log.info('{}: initialization.'.format(method_name))

        log.info('{}: return.'.format(method_name))
        return nltk.word_tokenize(sentence)

    def tokenize_sentences_from_file(self):
        method_name = "RawDataProcessor.tokenize_sentences_from_file"
        log.info('{}: initialization.'.format(method_name))
        data_now = datetime.datetime.now()
        output_filename = 'data/temp/tokens_' + str(time.mktime(data_now.timetuple())) + ".data"
        with open(output_filename, 'w') as o:
            with open(self._file_handler, 'r') as f:
                for line in f:
                    o.write(str(self.tokenize_sentence(line)) + '\n')
        print('Tokenized sentences saved at: {}.'.format(os.path.abspath(output_filename)))
        log.info('{}: return.'.format(method_name))

    def extract_sentences(self):
        method_name = "RawDataProcessor.extract_sentences"
        log.info('{}: initialization.'.format(method_name))
        data_now = datetime.datetime.now()
        output_filename = 'data/temp/sentences_' + str(time.mktime(data_now.timetuple())) + ".data"
        with open(output_filename, 'w') as o:
            with open(self._file_handler, 'r') as f:
                for line in f:
                    striped_sentences = line.split('.')
                    map(lambda x: o.write(' '.join(x.split())+'.\n'), [s.strip() for s in striped_sentences if len(s.strip()) > 0])
        log.info('{}: end.'.format(method_name))