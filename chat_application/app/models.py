from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(null=True,blank=True, max_length=2000)
    time = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)