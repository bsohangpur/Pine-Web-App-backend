# Generated by Django 4.2 on 2023-05-30 07:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0003_remove_blogs_post_alter_blogs_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='post',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
