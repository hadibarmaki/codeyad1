from django.db import models

# Create your models here.

class Footer(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    telegram = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)



class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    body = models.TextField()