from django.db import models





class Category(models.Model):
    title = models.CharField(max_length=50)
    theme = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title