from contextlib import nullcontext
from pyexpat import model
from django.db import models
from product.models import Product
from django.utils.translation import gettext as _
from phone_field import PhoneField

class Contact(models.Model):
    company_name = models.CharField(_("company name"),max_length=64)
    name = models.CharField(_("name"),max_length=64)
    email = models.EmailField(_("email"), max_length=120)
    phone = PhoneField(_("phone number"), blank=True)
    quantity = models.IntegerField(_("quantity"), null=True, blank=True)
    slug = models.SlugField(_("slug"), blank=True)
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE,null=True, related_name="inquery_product")
    service = models.ForeignKey("service.Service",verbose_name=_("service"), on_delete=models.CASCADE, null=True, related_name="inquery_service")
    description = models.TextField(_("description"), null=True, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    inquery_type = models.ForeignKey("contact.InQueryType",verbose_name=_("inquery type"), null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class InQueryType(models.Model):
    title = models.CharField(_("title"), max_length=64)
    active = models.BooleanField(_("active"), default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('InQuery Type')
        verbose_name_plural = _('InQuery Types')
