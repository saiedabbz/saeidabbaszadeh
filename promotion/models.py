from django.db import models
from django.utils.translation import gettext_lazy as _


class Promotion(models.Model):
    PERCENT = "PERCENT"
    AMOUNT = "AMOUNT"

    DISCOUNT_TYPES = (
        (PERCENT, PERCENT),
        (AMOUNT, AMOUNT)
    )

    ON_COllECTION = "ON_COLLECTION"
    ON_PRODUCT = "ON_PRODUCT"
    WITH_CODE = "WITH_CODE"

    PROMOTION_TYPE = (
        (ON_COllECTION, ON_COllECTION),
        (ON_PRODUCT, ON_PRODUCT),
        (WITH_CODE, WITH_CODE)
    )

    title = models.CharField(_("title"), null=True, blank=True, max_length=50)
    discount = models.IntegerField(_("discount"))
    discount_type = models.CharField(_("discount type"), choices=DISCOUNT_TYPES, max_length=50)
    start_at = models.DateTimeField(_("starts at"), auto_now=False, auto_now_add=False)
    end_at = models.DateTimeField(_("ends at"), auto_now=False, auto_now_add=False)
    promotion_type = models.CharField(_("promotion type"), choices=PROMOTION_TYPE, max_length=50)
    collections = models.ManyToManyField("product.Collection", verbose_name=_("collections"), related_name="promotions", blank=True)
    products = models.ManyToManyField("product.Product", verbose_name=_("products"), related_name="promotions", blank=True)
    code = models.CharField(_("code"), max_length=128, null=True, blank=True)
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Promotion')
        verbose_name_plural = _('Promotions')