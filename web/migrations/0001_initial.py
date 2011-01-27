
from south.db import db
from django.db import models
from qcdb.web.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Character'
        db.create_table('web_character', (
            ('id', orm['web.Character:id']),
            ('name', orm['web.Character:name']),
            ('bio', orm['web.Character:bio']),
            ('type', orm['web.Character:type']),
        ))
        db.send_create_signal('web', ['Character'])
        
        # Adding model 'Dialog'
        db.create_table('web_dialog', (
            ('id', orm['web.Dialog:id']),
            ('text', orm['web.Dialog:text']),
            ('panel', orm['web.Dialog:panel']),
            ('order', orm['web.Dialog:order']),
        ))
        db.send_create_signal('web', ['Dialog'])
        
        # Adding model 'Event'
        db.create_table('web_event', (
            ('id', orm['web.Event:id']),
            ('description', orm['web.Event:description']),
            ('comic', orm['web.Event:comic']),
        ))
        db.send_create_signal('web', ['Event'])
        
        # Adding model 'Comic'
        db.create_table('web_comic', (
            ('id', orm['web.Comic:id']),
            ('date', orm['web.Comic:date']),
            ('num', orm['web.Comic:num']),
            ('title', orm['web.Comic:title']),
            ('news', orm['web.Comic:news']),
            ('guest', orm['web.Comic:guest']),
            ('tags', orm['web.Comic:tags']),
        ))
        db.send_create_signal('web', ['Comic'])
        
        # Adding model 'GuestAuthor'
        db.create_table('web_guestauthor', (
            ('id', orm['web.GuestAuthor:id']),
            ('name', orm['web.GuestAuthor:name']),
            ('website', orm['web.GuestAuthor:website']),
        ))
        db.send_create_signal('web', ['GuestAuthor'])
        
        # Adding model 'Location'
        db.create_table('web_location', (
            ('id', orm['web.Location:id']),
            ('name', orm['web.Location:name']),
        ))
        db.send_create_signal('web', ['Location'])
        
        # Adding ManyToManyField 'Dialog.characters'
        db.create_table('web_dialog_characters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dialog', models.ForeignKey(orm.Dialog, null=False)),
            ('character', models.ForeignKey(orm.Character, null=False))
        ))
        
        # Adding ManyToManyField 'Comic.dialog'
        db.create_table('web_comic_dialog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comic', models.ForeignKey(orm.Comic, null=False)),
            ('dialog', models.ForeignKey(orm.Dialog, null=False))
        ))
        
        # Adding ManyToManyField 'Comic.locations'
        db.create_table('web_comic_locations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comic', models.ForeignKey(orm.Comic, null=False)),
            ('location', models.ForeignKey(orm.Location, null=False))
        ))
        
        # Adding ManyToManyField 'Comic.characters'
        db.create_table('web_comic_characters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comic', models.ForeignKey(orm.Comic, null=False)),
            ('character', models.ForeignKey(orm.Character, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Character'
        db.delete_table('web_character')
        
        # Deleting model 'Dialog'
        db.delete_table('web_dialog')
        
        # Deleting model 'Event'
        db.delete_table('web_event')
        
        # Deleting model 'Comic'
        db.delete_table('web_comic')
        
        # Deleting model 'GuestAuthor'
        db.delete_table('web_guestauthor')
        
        # Deleting model 'Location'
        db.delete_table('web_location')
        
        # Dropping ManyToManyField 'Dialog.characters'
        db.delete_table('web_dialog_characters')
        
        # Dropping ManyToManyField 'Comic.dialog'
        db.delete_table('web_comic_dialog')
        
        # Dropping ManyToManyField 'Comic.locations'
        db.delete_table('web_comic_locations')
        
        # Dropping ManyToManyField 'Comic.characters'
        db.delete_table('web_comic_characters')
        
    
    
    models = {
        'web.character': {
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'MAJOR'", 'max_length': '5'})
        },
        'web.comic': {
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Character']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dialog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Dialog']"}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.GuestAuthor']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Location']"}),
            'news': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.dialog': {
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'panel': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'web.event': {
            'comic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Comic']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'web.guestauthor': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'web.location': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['web']
