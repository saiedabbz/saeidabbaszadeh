from __future__ import unicode_literals
import sys

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Subscribe(models.Model):
    email = models.CharField(max_length=200, blank=True, null=True)


class StaticHtml(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.TextField()
    page_file = models.ImageField(upload_to = 'images/', default = 'product_category/None/no-img.jpg')

    def __str__(self):
        return self.title


class ItemType(models.Model):
    title = models.CharField(max_length=200, blank=False)


    def __str__(self):
        return self.title

class ItemTypeMapping(models.Model):
    itemType = models.ForeignKey(ItemType, blank=False, on_delete=models.CASCADE)
    fieldTitle = models.CharField(max_length=200)
    fieldType = models.IntegerField(blank=False, choices=[(1, 'Text Field'), (2, 'Text Area'), (3, 'Text Editor')])
    ordering = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.fieldTitle

class ItemCategory(models.Model):
    label = models.CharField(max_length=200)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class Item(models.Model):
    itemCategory = models.ForeignKey(ItemCategory, blank=True, on_delete=models.CASCADE)
    itemType = models.ForeignKey(ItemType, blank=False, on_delete=models.CASCADE)
    status = models.IntegerField(blank=True, default=0)

class ItemAddition(models.Model):
    item = models.ForeignKey(Item, blank=False, on_delete=models.CASCADE)
    itemTypeMapping = models.ForeignKey(ItemTypeMapping, on_delete=models.CASCADE)
    addition = models.TextField(blank=True, null=True)
