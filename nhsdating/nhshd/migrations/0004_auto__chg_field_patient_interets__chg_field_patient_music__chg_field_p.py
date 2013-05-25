# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Patient.interets'
        db.alter_column(u'nhshd_patient', 'interets', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.music'
        db.alter_column(u'nhshd_patient', 'music', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.food'
        db.alter_column(u'nhshd_patient', 'food', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.life_plan'
        db.alter_column(u'nhshd_patient', 'life_plan', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.favourite_things'
        db.alter_column(u'nhshd_patient', 'favourite_things', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.religion'
        db.alter_column(u'nhshd_patient', 'religion', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.what_im_looking_for'
        db.alter_column(u'nhshd_patient', 'what_im_looking_for', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.books'
        db.alter_column(u'nhshd_patient', 'books', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.preocupations'
        db.alter_column(u'nhshd_patient', 'preocupations', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.films'
        db.alter_column(u'nhshd_patient', 'films', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.skills'
        db.alter_column(u'nhshd_patient', 'skills', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Patient.other_things'
        db.alter_column(u'nhshd_patient', 'other_things', self.gf('django.db.models.fields.TextField')(default=''))

    def backwards(self, orm):

        # Changing field 'Patient.interets'
        db.alter_column(u'nhshd_patient', 'interets', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.music'
        db.alter_column(u'nhshd_patient', 'music', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.food'
        db.alter_column(u'nhshd_patient', 'food', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.life_plan'
        db.alter_column(u'nhshd_patient', 'life_plan', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.favourite_things'
        db.alter_column(u'nhshd_patient', 'favourite_things', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.religion'
        db.alter_column(u'nhshd_patient', 'religion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.what_im_looking_for'
        db.alter_column(u'nhshd_patient', 'what_im_looking_for', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.books'
        db.alter_column(u'nhshd_patient', 'books', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.preocupations'
        db.alter_column(u'nhshd_patient', 'preocupations', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.films'
        db.alter_column(u'nhshd_patient', 'films', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.skills'
        db.alter_column(u'nhshd_patient', 'skills', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Patient.other_things'
        db.alter_column(u'nhshd_patient', 'other_things', self.gf('django.db.models.fields.TextField')(null=True))

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
        u'nhshd.condition': {
            'Meta': {'object_name': 'Condition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'nhshd.healthcarelocation': {
            'Meta': {'object_name': 'HealthcareLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'nhshd.interest': {
            'Meta': {'object_name': 'Interest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'nhshd.patient': {
            'Meta': {'object_name': 'Patient'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'books': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'favourite_things': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'favourite_words': ('django.db.models.fields.TextField', [], {}),
            'films': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'food': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'healthcare_location': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nhshd.HealthcareLocation']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nhshd.Interest']", 'null': 'True', 'symmetrical': 'False'}),
            'interets': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'life_plan': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nhshd.Place']", 'null': 'True', 'symmetrical': 'False'}),
            'music': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'other_conditions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'other_condition'", 'null': 'True', 'to': u"orm['nhshd.Condition']"}),
            'other_things': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'personal_words': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nhshd.Photo']", 'null': 'True', 'blank': 'True'}),
            'preocupations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'primary_condition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_condition'", 'null': 'True', 'to': u"orm['nhshd.Condition']"}),
            'religion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skills': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'symptoms': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nhshd.Symptom']", 'null': 'True', 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'what_im_looking_for': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
