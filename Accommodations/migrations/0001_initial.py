# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Accommodation'
        db.create_table(u'Accommodations_accommodation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', max_length=500)),
            ('room_size', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('room_type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('main_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('price_per_day', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('price_per_month', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'Accommodations', ['Accommodation'])

        # Adding model 'AccommodationPhoto'
        db.create_table(u'Accommodations_accommodationphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=140, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('accommodation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='booking_accommodation', to=orm['Accommodations.Accommodation'])),
        ))
        db.send_create_signal(u'Accommodations', ['AccommodationPhoto'])

        # Adding model 'Booking'
        db.create_table(u'Accommodations_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checkin_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 10, 0, 0))),
            ('checkout_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 11, 0, 0))),
            ('status', self.gf('django.db.models.fields.CharField')(default='WFA', max_length=3)),
            ('tenant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='booking_tenant', to=orm['auth.User'])),
            ('accommodation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='booking_of_accommodation', to=orm['Accommodations.Accommodation'])),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'Accommodations', ['Booking'])


    def backwards(self, orm):
        # Deleting model 'Accommodation'
        db.delete_table(u'Accommodations_accommodation')

        # Deleting model 'AccommodationPhoto'
        db.delete_table(u'Accommodations_accommodationphoto')

        # Deleting model 'Booking'
        db.delete_table(u'Accommodations_booking')


    models = {
        u'Accommodations.accommodation': {
            'Meta': {'object_name': 'Accommodation'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price_per_day': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'price_per_month': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'room_size': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'room_type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'Accommodations.accommodationphoto': {
            'Meta': {'object_name': 'AccommodationPhoto'},
            'accommodation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'booking_accommodation'", 'to': u"orm['Accommodations.Accommodation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '140', 'blank': 'True'})
        },
        u'Accommodations.booking': {
            'Meta': {'object_name': 'Booking'},
            'accommodation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'booking_of_accommodation'", 'to': u"orm['Accommodations.Accommodation']"}),
            'checkin_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 12, 10, 0, 0)'}),
            'checkout_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 12, 11, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'WFA'", 'max_length': '3'}),
            'tenant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'booking_tenant'", 'to': u"orm['auth.User']"})
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

    complete_apps = ['Accommodations']