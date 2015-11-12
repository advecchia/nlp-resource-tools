import peewee as pw

database = pw.MySQLDatabase('mestrado', **{'password': 'mestrado', 'user': 'mestrado'})

class BaseModel(pw.Model):
    class Meta:
        database = database

class Files(BaseModel):
    id = pw.IntegerField(db_column='id', primary_key=True)
    language = pw.CharField(null=True, max_length=25)
    modified = pw.DateTimeField()
    name = pw.CharField(unique=True, max_length=150)
    parallel_file_id = pw.ForeignKeyField(db_column='parallel_file_id', rel_model='self', to_field='id')
    size = pw.IntegerField()

    class Meta:
        db_table = 'files'

class Paragraphs(BaseModel):
    file = pw.ForeignKeyField(db_column='file_id', rel_model=Files, to_field='id')
    order_in_file = pw.IntegerField()

    class Meta:
        db_table = 'paragraphs'

class Sentences(BaseModel):
    number_of_words = pw.IntegerField()
    order_in_paragraph = pw.IntegerField()
    paragraph = pw.ForeignKeyField(db_column='paragraph_id', rel_model=Paragraphs, to_field='id')

    class Meta:
        db_table = 'sentences'

class Tokens(BaseModel):
    id = pw.BigIntegerField(primary_key=True)
    lemma = pw.TextField()
    length = pw.IntegerField()
    order_in_sentence = pw.IntegerField()
    pos = pw.CharField()
    sentence = pw.ForeignKeyField(db_column='sentence_id', rel_model=Sentences, to_field='id')
    syllables = pw.TextField()
    synonyms = pw.TextField(null=True)
    tf_idf = pw.FloatField(null=True)
    token = pw.TextField()

    class Meta:
        db_table = 'tokens'

