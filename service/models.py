from django.db import models


class About(models.Model):
    image = models.FileField()
    description = models.CharField(max_length=100)
    libelle = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class Platfavori(models.Model):
    image = models.FileField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)


class Blog(models.Model):
    nom = models.CharField(max_length=(50))
    image = models.FileField()
    description = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)


class Menu(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.IntegerField()
    description = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)



