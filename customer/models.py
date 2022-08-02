from django.db import models
from django.utils.translation import gettext as _



class Customer(models.Model):
    title = models.CharField(_("title"), max_length=200)
    date_joined = models.DateField(_("date_joind"),auto_now_add=True)
    image = models.ImageField(_("image"), upload_to='customer/', blank=True, null=True)
    active = models.BooleanField(_("active"), default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

