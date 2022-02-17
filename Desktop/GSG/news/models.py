from distutils.command.upload import upload
from email.policy import default
from enum import unique
from pyexpat import model
from typing import Any
#from tinymce_4.fields import TinyMCEModelField
from django.db import models
from django.forms import FileField
from tinymce.models import HTMLField 
from autoslug import AutoSlugField
class News(models.Model):
    news_title=models.CharField(max_length=100)
    news_description=HTMLField()
    news_image = models.FileField(upload_to = 'news/', max_length=250, null=True, default = None)
    #news_slug = AutoSlugField(populate_from="news_title", unique=True, null=True, default=None)


# Create your models here.
