from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255,unique_for_date='Publishing_Time')
    content = models.TextField()
    author = models.ForeignKey(User,related_name='entries',blank=True,on_delete=models.CASCADE)
    Publishing_Time = models.DateTimeField(default=now)
    slug = models.SlugField(max_length=255, default='', blank=True)
    featured_image = models.ImageField(upload_to='static/featured_image/%Y/%M/%D/',blank=True)
    def __str__(self):
        return self.title + " by " + "'" + str(self.author) + "'"


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[:30] + "... " + "on Post: " + '"' + self.post.title + '"'
