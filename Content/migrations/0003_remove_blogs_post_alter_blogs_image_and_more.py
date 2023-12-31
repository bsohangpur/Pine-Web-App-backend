# Generated by Django 4.2 on 2023-05-30 07:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0002_alter_blogs_image_alter_services_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='post',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='careers',
            name='resume',
            field=models.FileField(help_text='Upload your PDF or DOC resume', upload_to='resume', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc'])], verbose_name='Resume'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='service'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='image',
            field=models.ImageField(upload_to='team'),
        ),
    ]
