from django.db import models
from django.core.validators import FileExtensionValidator, URLValidator

# Create your models here.
class Services(models.Model):
    image = models.ImageField(upload_to='media/service')
    title =models.CharField(max_length=255)
    detail = models.TextField()

class Teams(models.Model):
    image = models.ImageField(upload_to='media/team')
    title =models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    detail = models.TextField()

class Testimonials(models.Model):
    title =models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    message = models.TextField()

class Blogs(models.Model):
    slug = models.SlugField()
    image = models.ImageField(upload_to='media/blog')
    title =models.CharField(max_length=255)
    post=models.TextField()

class Newsletters(models.Model):
    email=models.EmailField()

class Careers(models.Model):
    name=models.CharField(max_length=255)
    phone=models.BigIntegerField()
    email = models.EmailField()
    message = models.TextField()
    resume = models.FileField(upload_to='media/resume', verbose_name='Resume', 
                                   help_text='Upload your PDF or DOC resume', 
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc'])])