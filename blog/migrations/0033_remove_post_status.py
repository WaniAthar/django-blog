# Generated by Django 3.2.3 on 2021-11-21 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
