from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(_("title"), max_length=64)
    slug = models.SlugField(_("slug"))
    image = models.ImageField(_("image"), upload_to='collections/', null=True, blank=True)
    image_top = models.ImageField(_("image_top"), upload_to='collections/', null=True, blank=True)
    body = RichTextField()
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    theme = models.CharField(_("Theme"), max_length=64, null=True, blank=True)


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Service, self).save(*args, **kwargs)


    def __str__(self):
        return self.title