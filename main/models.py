from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here
class Photo(models.Model):
    image = models.ImageField(upload_to = 'main/images/')
    
class Coach(models.Model):
    image = models.ImageField(upload_to= 'main/images/')
    name = models.CharField(max_length= 50)
    presentation = models.TextField(max_length= 250, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    
    
class Contact(models.Model):
    localisation = models.CharField(max_length=100)
    telephone = PhoneNumberField()
    email = models.EmailField()
    
class Presentation(models.Model):
    paragraphe = models.TextField(blank=True, max_length=255)
    
class Objectif(models.Model):
    liste = models.CharField(max_length=100)
    
    