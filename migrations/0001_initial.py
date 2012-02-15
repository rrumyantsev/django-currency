# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Currency'
        db.create_table('currencies_currency', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('factor', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=4)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('currencies', ['Currency'])


    def backwards(self, orm):
        
        # Deleting model 'Currency'
        db.delete_table('currencies_currency')


    models = {
        'currencies.currency': {
            'Meta': {'ordering': "['code']", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'factor': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '4'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['currencies']
