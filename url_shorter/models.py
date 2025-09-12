from django.db import models

# Create your models here.
class Shorter(models.Model):
    original_url = models.URLField(max_length=128,blank=True)
    url = models.URLField(max_length=128,unique=True,blank=True)