from django.db import models
from django.utils.translation import gettext as _
import uuid


def gen_id():
    return uuid.uuid4().hex


class BankTransaction(models.Model):
    INIT = 'INIT'
    FAILED = 'FAILED'
    SUCCEED = 'SUCCEED'

    STATS_LIST = [
        [INIT, INIT],
        [FAILED, FAILED],
        [SUCCEED, SUCCEED]
    ]

    id = models.CharField(_("id"), max_length=64, primary_key=True, default=gen_id)
    amount = models.BigIntegerField(_("amount"))
    description = models.TextField(_("description"), null=True, blank=True)
    ref_id = models.CharField(_("ref id"), max_length=50, null=True, blank=True)
    tracking_code = models.CharField(_("tracking code"), max_length=50, null=True, blank=True)
    card_number = models.CharField(_("card number"), max_length=50, null=True, blank=True)
    ip = models.CharField(_("ip"), max_length=50, null=True, blank=True)
    gateway_port = models.CharField(_("gateway port"), max_length=50, default="GARDESHPAY")
    status = models.CharField(_("status"), max_length=50, choices=STATS_LIST, default=INIT)
    callback = models.CharField(_('callback'), max_length=64)
    payment_date = models.DateTimeField(_("payment date"), null=True, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Bank Transaction'
        verbose_name_plural = 'Bank Transactions'

