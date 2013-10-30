# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'EspnSources', fields ['source_name']
        db.create_unique(u'app_espnsources', ['source_name'])


    def backwards(self, orm):
        # Removing unique constraint on 'EspnSources', fields ['source_name']
        db.delete_unique(u'app_espnsources', ['source_name'])


    models = {
        'app.br': {
            'Meta': {'object_name': 'Br'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 20, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.espnnews': {
            'Meta': {'object_name': 'EspnNews'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 20, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'headline': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'source': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Teams']", 'to_field': "'team_id'", 'null': 'True'})
        },
        'app.espnsources': {
            'Meta': {'object_name': 'EspnSources'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Teams']", 'to_field': "'team_id'", 'null': 'True'})
        },
        'app.teams': {
            'Meta': {'object_name': 'Teams'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'app.users': {
            'Meta': {'object_name': 'Users'},
            'facebook_access_token': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'facebook_access_token_expires': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'facebook_uid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Teams']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        }
    }

    complete_apps = ['app']