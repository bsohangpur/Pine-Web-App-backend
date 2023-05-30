from django.db import models
from django.core.validators import FileExtensionValidator, URLValidator
from ckeditor.fields import RichTextField


# Create your models here.
class Services(models.Model):
    image = models.ImageField(upload_to='service')
    title = models.CharField(max_length=255)
    detail = models.TextField()

    def __str__(self):
        return self.title


class Teams(models.Model):
    image = models.ImageField(upload_to='team')
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    detail = models.TextField()

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.title


class Blogs(models.Model):
    slug = models.SlugField()
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=255)
    summary = models.TextField(default='')
    post = RichTextField(default='')

    def __str__(self):
        return self.title


class Newsletters(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Careers(models.Model):
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    email = models.EmailField()
    message = models.TextField()
    resume = models.FileField(upload_to='resume', verbose_name='Resume',
                              help_text='Upload your PDF or DOC resume',
                              validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc'])])

    def __str__(self):
        return self.name
