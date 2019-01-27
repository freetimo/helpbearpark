from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

Choice = (
	('development', 'development'),
	('workout', 'workout'),
	('cooking', 'cooking')
)

class Directory(models.Model):
	choice = models.CharField(max_length=100, choices=Choice)
	title = models.CharField(max_length=200)
	slug = models.SlugField(allow_unicode=True, default='')
	thumbnail = ProcessedImageField(
		upload_to='directory/thumbnail/',
		options = {'quality': 80},
		processors=[ResizeToFill(300, 300)],
	)

	def __str__(self):
		return self.title

class Post(models.Model):
	directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name='posts')
	title = models.CharField(max_length=200)
	slug = models.SlugField(allow_unicode=True, default='')
	description = RichTextUploadingField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']
		

class Task(models.Model):
	title = models.CharField(max_length=250)
	user = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

class Contact(models.Model):
	title = models.CharField(max_length=250)
	email = models.EmailField(max_length=250)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']
		