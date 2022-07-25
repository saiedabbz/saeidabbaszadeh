from django.db import models
from django.utils.translation import gettext as _


class Order(models.Model):
    INIT = "INIT"
    CANCELLED = "CANCELLED"
    PAID = "PAID"
    PENDING = "PENDING"

    STATE_LIST = (
        (INIT, INIT),
        (CANCELLED, CANCELLED),
        (PAID, PAID),
        (PENDING, PENDING),
    )

    cart = models.ForeignKey("cart.Cart", verbose_name=_("cart"), on_delete=models.DO_NOTHING, null=True, blank=True)
    state = models.CharField(_("state"), choices=STATE_LIST, default=INIT, max_length=50)
    user = models.ForeignKey("user.User", verbose_name=_("user"), on_delete=models.DO_NOTHING, null=True, blank=True)
    address = models.ForeignKey("user.UserAddress", verbose_name=_("address"), on_delete=models.DO_NOTHING, null=True, blank=True)
    transaction = models.ForeignKey("payment_gateway.BankTransaction", verbose_name=_("bank transaction"), on_delete=models.DO_NOTHING,  null=True, blank=True)
    date = models.CharField(_("date"), null=True, blank=True, max_length=50)
    time = models.CharField(_("time"), null=True, blank=True, max_length=50)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.id} - {str(self.created_at)}"

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Order')


class OrderItem(models.Model):
    order = models.ForeignKey("order.Order", verbose_name=_("order"), on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey("product.ProductVariant", verbose_name=_("product variant"), on_delete=models.DO_NOTHING, null=True, blank=True)
    price = models.BigIntegerField(_("price"))
    promotion = models.ForeignKey("promotion.Promotion", verbose_name=_("promotion"), on_delete=models.DO_NOTHING, null=True, blank=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.order.id}"

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')
