# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'Activities_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'Activities', ['Location'])

        # Adding model 'Activity'
        db.create_table(u'Activities_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activity_author', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', max_length=500, null=True, blank=True)),
            ('activity_type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 12, 10, 0, 0))),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activity_location', to=orm['Activities.Location'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('attendees_limit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'Activities', ['Activity'])

        # Adding M2M table for field attendees on 'Activity'
        m2m_table_name = db.shorten_name(u'Activities_activity_attendees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'Activities.activity'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activity_id', 'user_id'])

        # Adding model 'Comment'
        db.create_table(u'Activities_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment_owner', to=orm['auth.User'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment_activity', to=orm['Activities.Activity'])),
            ('content', self.gf('django.db.models.fields.TextField')(default='', max_length=500)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 12, 9, 0, 0))),
        ))
        db.send_create_signal(u'Activities', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'Activities_location')

        # Deleting model 'Activity'
        db.delete_table(u'Activities_activity')

        # Removing M2M table for field attendees on 'Activity'
        db.delete_table(db.shorten_name(u'Activities_activity_attendees'))

        # Deleting model 'Comment'
        db.delete_table(u'Activities_comment')


    models = {
        u'Activities.activity': {
            'Meta': {'object_name': 'Activity'},
            'activity_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'attendees_limit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activity_location'", 'to': u"orm['Activities.Location']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activity_author'", 'to': u"orm['auth.User']"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 12, 10, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Activities.comment': {
            'Meta': {'object_name': 'Comment'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment_activity'", 'to': u"orm['Activities.Activity']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment_owner'", 'to': u"orm['auth.User']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 12, 9, 0, 0)'})
        },
        u'Activities.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Activities']