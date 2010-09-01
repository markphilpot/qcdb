from django.db import models

# Create your models here.
class Comic(models.Model):
	date = models.DateField('date published')
	url = models.URLField(max_length=200)
	num = models.IntegerField()
	title = models.CharField(max_length=200)
	news = models.TextField()
	guest = models.ForeignKey('Guest', null=True)
	characters = models.ManyToManyField('Character')
	locations = models.ManyToManyField('Location')
	tags = models.ManyToManyField('Tag')

class Character(models.Model):
	name = models.CharField(max_length=100)
	bio = models.TextField()

class Dialog(models.Model):
	characters = models.ManyToManyField('Character')
	text = models.TextField()
	panel = models.IntegerField()
	order = models.IntegerField()

class Guest(models.Model):
	name = models.CharField(max_length=100)
	website = models.CharField(max_length=200)

class Location(models.Model):
	name = models.CharField(max_length=100)

class Event(models.Model):
	description = models.CharField(max_length=200)
	comic = models.ForeignKey('Event')

class Tag(models.Model):
	tag = models.CharField(max_length=100)
