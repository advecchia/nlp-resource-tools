import logging as log

class Paragraph(object):
    def __init__(self, id, order_in_file, file_id):
        method_name = "Paragraph"
        log.info('{}: initialization.'.format(method_name))
        self._id = id
        self._order_in_file = order_in_file
        self._file_id = file_id
        log.info('{}: end.'.format(method_name))

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def order_in_file(self):
        return self._order_in_file
    @order_in_file.setter
    def order_in_file(self, order_in_file):
        self._order_in_file = order_in_file

    @property
    def file_id(self):
        return self._file_id
    @file_id.setter
    def file_id(self, file_id):
        self._file_id = file_id

    def __str__(self):
        return 'Paragraph: id={}, order_in_file={}, file_id={}'.format(self.id, self.order_in_file, self.file_id)
