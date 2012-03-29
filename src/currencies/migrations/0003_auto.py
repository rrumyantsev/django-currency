# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding index on 'Currency', fields ['code']
        db.create_index('currencies_currency', ['code'])


    def backwards(self, orm):
        
        # Removing index on 'Currency', fields ['code']
        db.delete_index('currencies_currency', ['code'])


    models = {
        'currencies.currency': {
            'Meta': {'ordering': "['code']", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_index': 'True'}),
            'factor': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '4'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['currencies']
