# Generated by Django 3.2.3 on 2021-11-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
    ]
