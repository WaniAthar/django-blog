from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    subject = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return "Message from " + self.name + " - " + self.subject 
