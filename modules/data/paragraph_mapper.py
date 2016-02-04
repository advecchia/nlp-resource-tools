import logging as log
from common_mapper import CommonMapper
from modules.data.storage import Paragraphs
from src.storage.paragraph import Paragraph

class ParagraphMapper(CommonMapper):
    def __init__(self):
        method_name = "ParagraphMapper"
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
    
    def insert(self, paragraph_object):
        method_name = 'ParagraphMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        query = Paragraphs.insert(file_id=paragraph_object.file_id, 
                             order_in_file=paragraph_object.order_in_file)
        paragraph_object.id = query.execute() # Return new id
        log.info('{}: end.'.format(method_name))
        return paragraph_object

    def update(self, paragraph_object):
        method_name = 'ParagraphMapper.update'
        log.info('{}: initialization.'.format(method_name))
        query = Paragraphs.update(file_id=paragraph_object.file_id, 
                             order_in_file=paragraph_object.order_in_file).where(Paragraphs.id==paragraph_object.id)
        log.info('{}: end.'.format(method_name))
        if query.execute() != 1: return True
        else: return False

    def get(self, paragraph_id):
        method_name = 'ParagraphMapper.get'
        log.info('{}: initialization.'.format(method_name))
        
        try:
            paragraph_object = Paragraphs.get(Paragraphs.id==paragraph_id)
            log.info('{}: end.'.format(method_name))
            return self.mapper(paragraph_object)
        except Exception as e:
            log.info('ParagraphNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))
            log.info('{}: end.'.format(method_name))
            raise Exception('ParagraphDoesNotExist errno={}: strerror{}.'.format(e.errno, e.strerror))

    def gets(self, file_id):
        method_name = 'ParagraphMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        paragraphs = []
        for db_paragraph in Paragraphs.select().where(Paragraphs.file_id==file_id):
            paragraphs.append(self.mapper(db_paragraph));
        log.info('{}: end.'.format(method_name))
        return paragraphs

    def mapper(self, db_paragraph):
        method_name = 'ParagraphMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        return Paragraph(identifier=db_paragraph.id, file_id=db_paragraph.file_id, 
                             order_in_file=db_paragraph.order_in_file)