# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Teams'
        db.create_table(u'app_teams', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal('app', ['Teams'])

        # Adding model 'EspnNews'
        db.create_table(u'app_espnnews', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('images', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Teams'], to_field='team_id', null=True)),
        ))
        db.send_create_signal('app', ['EspnNews'])

        # Adding model 'Br'
        db.create_table(u'app_br', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 9, 20, 0, 0))),
        ))
        db.send_create_signal('app', ['Br'])

        # Adding model 'EspnSources'
        db.create_table(u'app_espnsources', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Teams'], to_field='team_id', null=True)),
        ))
        db.send_create_signal('app', ['EspnSources'])

        # Adding model 'Users'
        db.create_table(u'app_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook_uid', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('user', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('facebook_access_token', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('facebook_access_token_expires', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('app', ['Users'])

        # Adding M2M table for field teams on 'Users'
        m2m_table_name = db.shorten_name(u'app_users_teams')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('users', models.ForeignKey(orm['app.users'], null=False)),
            ('teams', models.ForeignKey(orm['app.teams'], null=False))
        ))
        db.create_unique(m2m_table_name, ['users_id', 'teams_id'])


    def backwards(self, orm):
        # Deleting model 'Teams'
        db.delete_table(u'app_teams')

        # Deleting model 'EspnNews'
        db.delete_table(u'app_espnnews')

        # Deleting model 'Br'
        db.delete_table(u'app_br')

        # Deleting model 'EspnSources'
        db.delete_table(u'app_espnsources')

        # Deleting model 'Users'
        db.delete_table(u'app_users')

        # Removing M2M table for field teams on 'Users'
        db.delete_table(db.shorten_name(u'app_users_teams'))


    models = {
        'app.br': {
            'Meta': {'object_name': 'Br'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 20, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.espnnews': {
            'Meta': {'object_name': 'EspnNews'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Teams']", 'to_field': "'team_id'", 'null': 'True'})
        },
        'app.espnsources': {
            'Meta': {'object_name': 'EspnSources'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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