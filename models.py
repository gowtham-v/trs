import datetime
from django.utils import timezone
from django.db import models
class Poll(models.Model):
	qn = models.CharField(max_length=200)
	pub_date = models.DateTimeField('today')
	def __unicode__(self):
		return self.qn
	def was_pubs_recent(self):
		return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
	was_pubs_recent.admin_order_field = 'pub_date'
	was_pubs_recent.boolean = True
     was_pubs_recent.short_description = 'Published recently?'
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
   	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.choice_text

# Create your models here.
