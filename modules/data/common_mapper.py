from abc import ABCMeta, abstractmethod
import logging as log

class CommonMapper(object):
    """An abstract common mapper class for the database data types.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        method_name = 'CommonMapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))

    @abstractmethod
    def insert(self):
        method_name = 'CommonMapper.insert'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        raise NotImplementedError('Not implemented yet')
    
    @abstractmethod
    def update(self):
        method_name = 'CommonMapper.update'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        raise NotImplementedError('Not implemented yet')
    
    @abstractmethod
    def get(self):
        method_name = 'CommonMapper.get'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        raise NotImplementedError('Not implemented yet')
    
    @abstractmethod
    def gets(self):
        method_name = 'CommonMapper.gets'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        raise NotImplementedError('Not implemented yet')
    
    @abstractmethod
    def mapper(self):
        method_name = 'CommonMapper.mapper'
        log.info('{}: initialization.'.format(method_name))
        log.info('{}: end.'.format(method_name))
        raise NotImplementedError('Not implemented yet')