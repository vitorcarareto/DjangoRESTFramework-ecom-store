from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    products = models.ManyToManyField(Products)
