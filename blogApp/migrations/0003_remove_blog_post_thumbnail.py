# Generated by Django 4.0.5 on 2022-08-03 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_blog_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='thumbnail',
        ),
    ]
