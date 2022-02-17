import email
from email import message
from os import name
from pyexpat import model
from django.db import models

# Create your models here.
class ContactPage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    