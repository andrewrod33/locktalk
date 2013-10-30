# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EspnSources'
        db.delete_table(u'app_espnsources')

        # Deleting model 'EspnNews'
        db.delete_table(u'app_espnnews')

        # Adding model 'Sources'
        db.create_table(u'app_sources', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('app', ['Sources'])

        # Adding model 'News'
        db.create_table(u'app_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('source', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('images', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Teams'], to_field='team_id', null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 9, 24, 0, 0))),
        ))
        db.send_create_signal('app', ['News'])


    def backwards(self, orm):
        # Adding model 'EspnSources'
        db.create_table(u'app_espnsources', (
            ('source_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Teams'], to_field='team_id', null=True)),
        ))
        db.send_create_signal('app', ['EspnSources'])

        # Adding model 'EspnNews'
        db.create_table(u'app_espnnews', (
            ('headline', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('source', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 9, 24, 0, 0))),
            ('images', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Teams'], to_field='team_id', null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('app', ['EspnNews'])

        # Deleting model 'Sources'
        db.delete_table(u'app_sources')

        # Deleting model 'News'
        db.delete_table(u'app_news')


    models = {
        'app.br': {
            'Meta': {'object_name': 'Br'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 24, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.news': {
            'Meta': {'object_name': 'News'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 24, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'headline': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'source': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Teams']", 'to_field': "'team_id'", 'null': 'True'})
        },
        'app.sources': {
            'Meta': {'object_name': 'Sources'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
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