from django.db import models

# Create your models here.
class Comic(models.Model):
	date = models.DateField('date published', null=True, blank=True)
	num = models.IntegerField()
	title = models.CharField(max_length=200)
	news = models.TextField(blank=True)
	guest = models.ForeignKey('GuestAuthor', null=True, blank=True)
	characters = models.ManyToManyField('Character')
	locations = models.ManyToManyField('Location')
	tags = models.CharField(max_length=200, blank=True)
	dialog = models.ManyToManyField('Dialog', related_name="comic")

	def __unicode__(self):
		return "%i :: %s" % (self.num, self.title)

class Character(models.Model):
	name = models.CharField(max_length=100)
	bio = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class Dialog(models.Model):
	characters = models.ManyToManyField('Character')
	text = models.TextField()
	panel = models.IntegerField()
	order = models.IntegerField()

	#class Meta:
	#	ordering = ('panel','order')

	def charList(self):
		strList = []
		for char in self.characters.all():
			strList.append(char.name)
			strList.append(", ")
		strList.pop()
		return ''.join(strList)

	def __unicode__(self):
		strList = []
		if self.comic.count() != 0:
			strList.append("%i" % self.comic.all()[0].num)
		else:
			strList.append("__")
		strList.append("::")
		strList.append("%i-%i " % (self.panel,self.order))
		for char in self.characters.all():
			strList.append(char.name)
			strList.append(", ")
		strList.pop()
		strList.append(" :: ")
		strList.append(self.text[0:50])
		return ''.join(strList)



class GuestAuthor(models.Model):
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
	comic = models.ForeignKey('Comic')

	def __unicode__(self):
		return self.description
