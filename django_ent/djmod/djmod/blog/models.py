from django.db import models
from django.utils import timezone  
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.utils.timesince import timesince
from datetime import timedelta, datetime, date


def validate_author_email(value):
	if "@" in value:
		return value
	else:
		raise ValidationError("Not a valid email")



PUBLISH_CHOICES = (
	('draft', 'Draft'),
	('publish','Publish'),
	('private', 'Private'),
	)
# Create your models here.
class PostModel(models.Model):
	id= models.BigAutoField(primary_key= True)
	active= models.BooleanField(default= True)
	title = models.CharField(max_length=250,unique= True)
	content= models.TextField(null= True, blank= True)
	publish =models.CharField(max_length=120, choices=PUBLISH_CHOICES,default='draft')
	view_count= models.IntegerField(default=0)
	publish_date= models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)
	author_email= models.CharField(max_length=240, validators=[validate_author_email],null=True, blank=True)
	slug=models.SlugField(null=True, blank=True)
	updated= models.DateTimeField(auto_now= True, )
	timestamp= models.DateTimeField(auto_now_add= True)
	
	class Meta:
		verbose_name= 'Post'
		verbose_name_plural= 'Posts'


	# def save(self, *args, **kwargs):
		# print("hello there")
		# self.title= "new Title"
		# if not self.slug:
		# 	self.slug= slugify(self.title)
		# super(PostModel, self).save(*args, **kwargs)


	def __unicode__(self):       #python 2
		return (self.title)

	def __str__(self):
		return (self.title)        #python3

	def age(self):
		if self.publish =='publish':

			now = datetime.now()
			publish_time= datetime.combine(
				self.publish_date, 
				datetime.now().min.time())
			try:
				difference =now- publish_time
			except:
				return "Unknow"

			if difference <= timedelta(minutes=1):
				return 'just now'
			return '{time} ago'.format(time= timesince(publish_time).split(',')[0])
		return "not published"

def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
	print("before save")
	if not instance.slug and instance.title:
		instance.slug= slugify(instance.title)
pre_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)

def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
	print("after save")
	print(created)
	if created:
		if not instance.slug and instance.title:
			instance.slug= slugify(instance.title)
			instance.save()
post_save.connect(blog_post_model_post_save_receiver, sender=PostModel)


