from django.contrib import admin
from .models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'discount',
        'discount_type',
        'start_at',
        'end_at',
        'promotion_type',
    ]
