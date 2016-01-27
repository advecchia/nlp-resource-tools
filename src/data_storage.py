from peewee import *

database = MySQLDatabase('mestrado', **{'password': 'mestrado', 'user': 'mestrado'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Languages(BaseModel):
    acronym = CharField()
    title = CharField()

    class Meta:
        db_table = 'languages'

class Files(BaseModel):
    language = ForeignKeyField(db_column='language_id', null=True, rel_model=Languages, to_field='id')
    modified = DateTimeField(null=True)
    name = CharField(unique=True)
    parallel_file = ForeignKeyField(db_column='parallel_file_id', null=True, rel_model='self', to_field='id')
    size = IntegerField()

    class Meta:
        db_table = 'files'

class PartOfSpeech(BaseModel):
    acronym = CharField()
    language = ForeignKeyField(db_column='language_id', rel_model=Languages, to_field='id')
    name = CharField()

    class Meta:
        db_table = 'part_of_speech'

class Lemmas(BaseModel):
    id = BigIntegerField(primary_key=True)
    lemma = TextField()
    length = IntegerField()
    pos = ForeignKeyField(db_column='pos_id', rel_model=PartOfSpeech, to_field='id')
    syllables = TextField()

    class Meta:
        db_table = 'lemmas'

class Paragraphs(BaseModel):
    file = ForeignKeyField(db_column='file_id', rel_model=Files, to_field='id')
    id = BigIntegerField(primary_key=True)
    order_in_file = IntegerField()

    class Meta:
        db_table = 'paragraphs'

class Tokens(BaseModel):
    id = BigIntegerField(primary_key=True)
    lemma = ForeignKeyField(db_column='lemma_id', rel_model=Lemmas, to_field='id')
    length = IntegerField()
    pos = ForeignKeyField(db_column='pos_id', rel_model=PartOfSpeech, to_field='id')
    syllabes = TextField()
    token = TextField()

    class Meta:
        db_table = 'tokens'

class Senses(BaseModel):
    related_token = ForeignKeyField(db_column='related_token_id', rel_model=Tokens, to_field='id')
    sense_type = CharField()
    token = ForeignKeyField(db_column='token_id', rel_model=Tokens, related_name='tokens_token_set', to_field='id')

    class Meta:
        db_table = 'senses'
        primary_key = CompositeKey('related_token', 'token')

class Sentences(BaseModel):
    id = BigIntegerField(primary_key=True)
    number_of_words = IntegerField()
    order_in_paragraph = IntegerField()
    paragraph = ForeignKeyField(db_column='paragraph_id', rel_model=Paragraphs, to_field='id')

    class Meta:
        db_table = 'sentences'

class TokensPerFile(BaseModel):
    count = IntegerField()
    file = ForeignKeyField(db_column='file_id', rel_model=Files, to_field='id')
    token = ForeignKeyField(db_column='token_id', rel_model=Tokens, to_field='id')

    class Meta:
        db_table = 'tokens_per_file'
        primary_key = CompositeKey('file', 'token')

class TokensPerSentence(BaseModel):
    id = BigIntegerField(primary_key=True)
    order_in_sentence = IntegerField()
    sentence = ForeignKeyField(db_column='sentence_id', rel_model=Sentences, to_field='id')
    token = ForeignKeyField(db_column='token_id', rel_model=Tokens, to_field='id')

    class Meta:
        db_table = 'tokens_per_sentence'

