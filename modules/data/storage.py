import peewee as pw

database = pw.MySQLDatabase('mestrado', **{'password': 'mestrado', 'user': 'mestrado'})

class UnknownField(object):
    pass

class BaseModel(pw.Model):
    class Meta:
        database = database

class Languages(BaseModel):
    id = pw.IntegerField(db_column='id', primary_key=True)
    acronym = pw.CharField(max_length=10)
    title = pw.CharField(max_length=40)

    class Meta:
        db_table = 'languages'

class Files(BaseModel):
    id = pw.IntegerField(db_column='id', primary_key=True)
    parallel_file_id = pw.ForeignKeyField(db_column='parallel_file_id', null=True, rel_model='self', to_field='id')
    name = pw.CharField(unique=True, max_length=150)
    size = pw.IntegerField()
    modified = pw.DateTimeField(null=True)
    language_id = pw.ForeignKeyField(db_column='language_id', null=True, rel_model=Languages, to_field='id')

    class Meta:
        db_table = 'files'

class PartsOfSpeech(BaseModel):
    id = pw.IntegerField(db_column='id', primary_key=True)
    tag = pw.CharField(max_length=10)
    description = pw.CharField(max_length=100)
    language_id = pw.ForeignKeyField(db_column='language_id', rel_model=Languages, to_field='id')

    class Meta:
        db_table = 'part_of_speech'

class Lemmas(BaseModel):
    id = pw.BigIntegerField(primary_key=True)
    lemma = pw.TextField()
    pos_id = pw.ForeignKeyField(db_column='pos_id', rel_model=PartsOfSpeech, to_field='id')
    syllables = pw.TextField()
    length = pw.IntegerField()

    class Meta:
        db_table = 'lemmas'

class Paragraphs(BaseModel):
    id = pw.BigIntegerField(primary_key=True)
    file_id = pw.ForeignKeyField(db_column='file_id', rel_model=Files, to_field='id')
    order_in_file = pw.IntegerField()

    class Meta:
        db_table = 'paragraphs'

class Sentences(BaseModel):
    id = pw.BigIntegerField(primary_key=True)
    paragraph_id = pw.ForeignKeyField(db_column='paragraph_id', rel_model=Paragraphs, to_field='id')
    number_of_words = pw.IntegerField()
    order_in_paragraph = pw.IntegerField()

    class Meta:
        db_table = 'sentences'

class Tokens(BaseModel):
    id = pw.BigIntegerField(primary_key=True)
    token = pw.TextField()
    lemma_id = pw.ForeignKeyField(db_column='lemma_id', rel_model=Lemmas, to_field='id')
    pos_id = pw.ForeignKeyField(db_column='pos_id', rel_model=PartsOfSpeech, to_field='id')
    order_in_sentence = pw.IntegerField()
    syllables = pw.TextField()
    length = pw.IntegerField()

    class Meta:
        db_table = 'tokens'

class Senses(BaseModel):
    token_id = pw.ForeignKeyField(db_column='token_id', rel_model=Tokens, related_name='tokens_token_set', to_field='id')
    related_token_id = pw.ForeignKeyField(db_column='related_token_id', rel_model=Tokens, to_field='id')
    sense_type = pw.CharField()
    correlation = pw.FloatField()

    class Meta:
        db_table = 'senses'
        primary_key = pw.CompositeKey('token_id', 'related_token_id')

class TokensPerFile(BaseModel):
    file_id = pw.ForeignKeyField(db_column='file_id', rel_model=Files, to_field='id')
    token_id = pw.ForeignKeyField(db_column='token_id', rel_model=Tokens, to_field='id')
    count = pw.IntegerField()

    class Meta:
        db_table = 'tokens_per_file'
        primary_key = pw.CompositeKey('file_id', 'token_id')

class TokensPerSentence(BaseModel):
    id = pw.BigIntegerField(primary_key=True)
    sentence_id = pw.ForeignKeyField(db_column='sentence_id', rel_model=Sentences, to_field='id')
    token_id = pw.ForeignKeyField(db_column='token_id', rel_model=Tokens, to_field='id')
    order_in_sentence = pw.IntegerField()

    class Meta:
        db_table = 'tokens_per_sentence'
