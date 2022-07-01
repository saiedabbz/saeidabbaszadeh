from unicodedata import category
from django.db import models

from default.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name