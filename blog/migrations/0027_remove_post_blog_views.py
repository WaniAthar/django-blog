# Generated by Django 3.2.3 on 2021-11-21 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_post_blog_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blog_views',
        ),
    ]
