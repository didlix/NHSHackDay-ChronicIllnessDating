# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'nhshd_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nhshd.Photo'], null=True)),
            ('personal_words', self.gf('django.db.models.fields.TextField')()),
            ('favourite_words', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nhshd', ['Patient'])

        # Adding M2M table for field locations on 'Patient'
        m2m_table_name = db.shorten_name(u'nhshd_patient_locations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('patient', models.ForeignKey(orm[u'nhshd.patient'], null=False)),
            ('place', models.ForeignKey(orm[u'nhshd.place'], null=False))
        ))
        db.create_unique(m2m_table_name, ['patient_id', 'place_id'])

        # Adding M2M table for field symptoms on 'Patient'
        m2m_table_name = db.shorten_name(u'nhshd_patient_symptoms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('patient', models.ForeignKey(orm[u'nhshd.patient'], null=False)),
            ('symptom', models.ForeignKey(orm[u'nhshd.symptom'], null=False))
        ))
        db.create_unique(m2m_table_name, ['patient_id', 'symptom_id'])

        # Adding M2M table for field interests on 'Patient'
        m2m_table_name = db.shorten_name(u'nhshd_patient_interests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('patient', models.ForeignKey(orm[u'nhshd.patient'], null=False)),
            ('interest', models.ForeignKey(orm[u'nhshd.interest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['patient_id', 'interest_id'])

        # Adding model 'Place'
        db.create_table(u'nhshd_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'nhshd', ['Place'])

        # Adding model 'Interest'
        db.create_table(u'nhshd_interest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'nhshd', ['Interest'])

        # Adding model 'Symptom'
        db.create_table(u'nhshd_symptom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'nhshd', ['Symptom'])

        # Adding model 'Photo'
        db.create_table(u'nhshd_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'nhshd', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'nhshd_patient')

        # Removing M2M table for field locations on 'Patient'
        db.delete_table(db.shorten_name(u'nhshd_patient_locations'))

        # Removing M2M table for field symptoms on 'Patient'
        db.delete_table(db.shorten_name(u'nhshd_patient_symptoms'))

        # Removing M2M table for field interests on 'Patient'
        db.delete_table(db.shorten_name(u'nhshd_patient_interests'))

        # Deleting model 'Place'
        db.delete_table(u'nhshd_place')

        # Deleting model 'Interest'
        db.delete_table(u'nhshd_interest')

        # Deleting model 'Symptom'
        db.delete_table(u'nhshd_symptom')

        # Deleting model 'Photo'
        db.delete_table(u'nhshd_photo')


    models = {
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'nhshd.interest': {
            'Meta': {'object_name': 'Interest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'nhshd.patient': {
            'Meta': {'object_name': 'Patient'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'favourite_words': ('django.db.models.fields.TextField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nhshd.Interest']", 'null': 'True', 'symmetrical': 'False'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nhshd.Place']", 'null': 'True', 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'personal_words': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nhshd.Photo']", 'null': 'True'}),
            'symptoms': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nhshd.Symptom']", 'null': 'True', 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'nhshd.photo': {
            'Meta': {'object_name': 'Photo'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'nhshd.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'nhshd.symptom': {
            'Meta': {'object_name': 'Symptom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['nhshd']