from peewee import *

database = MySQLDatabase('mestrado', **{'password': 'mestrado', 'user': 'mestrado'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Files(BaseModel):
    language = CharField(null=True)
    modified = DateTimeField()
    name = CharField(unique=True)
    parallel_file = ForeignKeyField(db_column='parallel_file_id', rel_model='self', to_field='id')
    size = IntegerField()

    class Meta:
        db_table = 'files'

class Paragraphs(BaseModel):
    file = ForeignKeyField(db_column='file_id', rel_model=Files, to_field='id')
    order_in_file = IntegerField()

    class Meta:
        db_table = 'paragraphs'

class Sentences(BaseModel):
    number_of_words = IntegerField()
    order_in_paragraph = IntegerField()
    paragraph = ForeignKeyField(db_column='paragraph_id', rel_model=Paragraphs, to_field='id')

    class Meta:
        db_table = 'sentences'

class Tokens(BaseModel):
    id = BigIntegerField(primary_key=True)
    lemma = TextField()
    length = IntegerField()
    order_in_sentence = IntegerField()
    pos = CharField()
    sentence = ForeignKeyField(db_column='sentence_id', rel_model=Sentences, to_field='id')
    syllables = TextField()
    synonyms = TextField(null=True)
    tf_idf = FloatField(null=True)
    token = TextField()

    class Meta:
        db_table = 'tokens'

