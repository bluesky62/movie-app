from email.policy import default
from enum import unique
from pyexpat import model
from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_discription = models.TextField()
    #service_slug= AutoSlugField(populate_from="service_title", unique=True, null=True, default=None)
    
     