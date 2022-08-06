from contextlib import nullcontext
from pyexpat import model
from django.db import models
from product.models import Product
from django.utils.translation import gettext as _
from phone_field import PhoneField

class Contact(models.Model):
    company_name = models.CharField(_("company name"),max_length=64)
    first_name = models.CharField(_("first name"),max_length=64)
    last_name = models.CharField(_("last name"), max_length=64)
    email = models.EmailField(_("email"), max_length=120)
    phone = PhoneField(_("phone number"), blank=True)
    quantity = models.IntegerField(_("quantity"), null=True, blank=True, default=True)
    slug = models.SlugField(_("slug"))
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE, related_name="contact")
    description = models.TextField(_("description"), null=True, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    contact_type = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
