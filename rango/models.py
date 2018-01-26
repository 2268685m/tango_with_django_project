from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)

	class Meta:
                verbose_name_plural = 'Categroies'
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
		
	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.name
		
		
class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __str__(self): # For Python 2, use __unicode__too
		return self.title

	def __unicode__(self): # For Python 2, use __unicode__too
		return self.title
