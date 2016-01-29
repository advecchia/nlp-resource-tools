import logging as log

class Sense(object):
    def __init__(self, token_id, related_token_id, sense_type):
        method_name = "Sense"
        log.info('{}: initialization.'.format(method_name))
        self._token_id = token_id
        self._related_token_id = related_token_id
        self._sense_type = sense_type
        log.info('{}: end.'.format(method_name))

    @property
    def token_id(self):
        return self._token_id
    @token_id.setter
    def token_id(self, token_id):
        self._token_id = token_id

    @property
    def related_token_id(self):
        return self._related_token_id
    @related_token_id.setter
    def related_token_id(self, related_token_id):
        self._related_token_id = related_token_id

    @property
    def sense_type(self):
        return self._sense_type
    @sense_type.setter
    def sense_type(self, sense_type):
        self._sense_type = sense_type

    def __str__(self):
        return 'Sense: token_id={}, related_token_id={}, sense_type={}'.format(self.token_id, self.related_token_id, self.sense_type)