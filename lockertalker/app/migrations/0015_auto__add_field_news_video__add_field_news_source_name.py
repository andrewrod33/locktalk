# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.video'
        db.add_column(u'app_news', 'video',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'News.source_name'
        db.add_column(u'app_news', 'source_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.video'
        db.delete_column(u'app_news', 'video')

        # Deleting field 'News.source_name'
        db.delete_column(u'app_news', 'source_name')


    models = {
        'app.br': {
            'Meta': {'object_name': 'Br'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.news': {
            'Meta': {'object_name': 'News'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 6, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'headline': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Sources']", 'null': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Teams']", 'to_field': "'team_id'", 'null': 'True'}),
            'video': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'app.personalizedsource': {
            'Meta': {'object_name': 'PersonalizedSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_id': ('django.db.models.fields.IntegerField', [], {'default': "''"}),
            'source_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'app.sources': {
            'Meta': {'object_name': 'Sources'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'app.teams': {
            'Meta': {'object_name': 'Teams'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Sources']", 'symmetrical': 'False'}),
            'team_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'app.userblockssources': {
            'Meta': {'object_name': 'UserBlocksSources'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['app.Sources']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['app.Teams']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'user_blocks'", 'to': "orm['app.Users']"})
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