from json import load
from django.db import models

class Banner(models.Model):
    image = models.FileField(upload_to="image_banner")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)


class Contact(models.Model):
     nom = models.CharField(max_length=50)
     email = models.EmailField(max_length=254)
     message = models.CharField(max_length=300)
     create_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)
     statut = models.BooleanField(default=True)

class Reseausocial(models.Model):
    nom = models.CharField(max_length=50)
    Icon = models.CharField(max_length=100)
    lien = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class newletter(models.Model):
    email = models.EmailField(max_length=254)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class About(models.Model):
    image = models.FileField()
    description = models.CharField(max_length=100)
    libelle = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)









