from django.db import models
from django.utils.translation import gettext as _


class Cart(models.Model):
    user = models.ForeignKey("user.User", verbose_name=_("user"), on_delete=models.CASCADE)
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')


class CartItem(models.Model):
    cart = models.ForeignKey("cart.Cart", verbose_name=_("cart"), on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey("product.ProductVariant", verbose_name=_("product variant"), on_delete=models.CASCADE)
    amount = models.IntegerField(_("amount"), default=1)

    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.variant.product.title} - {list(self.variant.options.all().values_list('value', flat=True))} - {self.amount}"

    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')
