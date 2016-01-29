import logging as log

class Paragraph(object):
    def __init__(self, identifier, file_id, order_in_file):
        method_name = "Paragraph"
        log.info('{}: initialization.'.format(method_name))
        self._id = identifier
        self._file_id = file_id
        self._order_in_file = order_in_file
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, identifier):
        self._id = identifier

    @property
    def file_id(self):
        return self._file_id
    @file_id.setter
    def file_id(self, file_id):
        self._file_id = file_id

    @property
    def order_in_file(self):
        return self._order_in_file
    @order_in_file.setter
    def order_in_file(self, order_in_file):
        self._order_in_file = order_in_file

    def __str__(self):
        return 'Paragraph: id={}, file_id={}, order_in_file={}'.format(self.id, self.file_id, self.order_in_file)
