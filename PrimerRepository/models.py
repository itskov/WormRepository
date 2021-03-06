from django.db import models

# Create your models here.
# Fridge class.
class Primer(models.Model):
	name = models.CharField('Name', max_length=256)
	created_on_date = models.DateTimeField('Date Added', default=datetime.now())
	user = models.ForeignKey(User)
	
	sequence = models.TextField('Sequence')
	
	def __unicode__(self):
		return self.name
