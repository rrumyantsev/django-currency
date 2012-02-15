# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Currency.symbol'
        db.delete_column('currencies_currency', 'symbol')

        # Deleting field 'Currency.is_active'
        db.delete_column('currencies_currency', 'is_active')


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Currency.symbol'
        raise RuntimeError("Cannot reverse this migration. 'Currency.symbol' and its values cannot be restored.")

        # Adding field 'Currency.is_active'
        db.add_column('currencies_currency', 'is_active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    models = {
        'currencies.currency': {
            'Meta': {'ordering': "['code']", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'factor': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '4'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['currencies']
