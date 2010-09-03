from django.db import models

# Create your models here.
class Comic(models.Model):
	date = models.DateField('date published', null=True, blank=True)
	num = models.IntegerField()
	title = models.CharField(max_length=200)
	news = models.TextField(blank=True)
	guest = models.ForeignKey('Guest', null=True, blank=True)
	characters = models.ManyToManyField('Character')
	locations = models.ManyToManyField('Location')
	tags = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return self.title

class Character(models.Model):
	name = models.CharField(max_length=100)
	bio = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name

class Dialog(models.Model):
	comic = models.ForeignKey('Comic')
	characters = models.ManyToManyField('Character')
	text = models.TextField()
	panel = models.IntegerField()
	order = models.IntegerField()
	
	def __unicode__(self):
		strList = []
		for char in self.characters:
			strList.append(char.name)
			strList.append(", ")
		strList.pop()
		strList.append(" :: ")
		strList.append(self.text)
		return ''.join(strList)
		
			

class Guest(models.Model):
	name = models.CharField(max_length=100)
	website = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class Event(models.Model):
	description = models.CharField(max_length=200)
	comic = models.ForeignKey('Event')
