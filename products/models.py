from cocktails.models import Alcohol, AttachedMaterial
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class AlcoholicProduct(models.Model):
    name = models.CharField(max_length=100)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])


class OtherProduct(models.Model):
    name = models.CharField(max_length=100)
    attached_material = models.ForeignKey(
        AttachedMaterial, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
