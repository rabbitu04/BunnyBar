from django.db import models

# Create your models here.
ALCOHOL_TYPES = [
    ('Rum', 'Rum'),
    ('Brandy', 'Brandy'),
    ('Tequila', 'Tequila'),
    ('Whisky', 'Whisky'),
    ('Vodka', 'Vodka'),
    ('Gin', 'Gin'),
    ('Liqueur', 'Liqueur'),
    ('Beer', 'Beer'),
    ('Wine', 'Wine'),
    ('Champagne', 'Champagne'),
    ('Vermouth', 'Vermouth'),
    ('Absinthe', 'Absinthe'),
    ('Bitters', 'Bitters'),
    ('Sake', 'Sake'),
    ('Soju', 'Soju'),
    ('Others', 'Others'),
]


class Alcohol(models.Model):
    name = models.CharField(max_length=100, unique=True)
    alcohol_type = models.CharField(max_length=10, choices=ALCOHOL_TYPES)


class AttachedMaterial(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Cocktail(models.Model):
    name = models.CharField(max_length=100, unique=True)
    recipe = models.TextField(max_length=200)
    alcohols = models.ManyToManyField(Alcohol)
    attached_materials = models.ManyToManyField(
        AttachedMaterial, blank=True)
    image = models.ImageField(upload_to='static/images/', null=True)
