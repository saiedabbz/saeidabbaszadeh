from django.contrib import admin
from .models import (
    Product, ProductImage, ProductOption, ProductOptionGroup, ProductVariant, Showcase,
    Collection, CollectionType, ProductExtra
)

from django.utils.html import format_html

from django.utils.translation import gettext_lazy as _


class VariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 0
    verbose_name = _("Product Variant")
    verbose_name_plural = _("Product Variants")

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    verbose_name = _("Image")
    verbose_name_plural = _("Images")

class ProductExtraInline(admin.TabularInline):
    model = ProductExtra
    extra = 0
    verbose_name = _("Extra")
    verbose_name_plural = _("Extras")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
        'description',
        'collection_titles',
        'active',
        'created_at',
    ]

    

    def collection_titles(self, obj):
        return f"{list(obj.collections.all().values_list('title', flat=True))}"

    inlines = [
        VariantInline,
        ProductImageInline,
        ProductExtraInline,
    ]


@admin.register(Showcase)
class ShowcaseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_title',
        'title',
        'active',
        'created_at',
    ]

    def product_title(self, obj):
        return obj.product.title

    def option_list(self, obj):
        return f"{list(obj.options.all().values_list('value', flat=True))}"


@admin.register(ProductVariant)
class VariantAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_title',
        'option_list',
        'stock',
        'price',
        'is_main',
        'active',
        'created_at',
    ]

    def product_title(self, obj):
        return obj.product.title

    def option_list(self, obj):
        return f"{list(obj.options.all().values_list('value', flat=True))}"


@admin.register(ProductOptionGroup)
class OptionGroupAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'field',
        'active',
        'created_at',
    ]


@admin.register(ProductOption)
class OptionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'field',
        'value',
        'active',
        'created_at',
    ]

    def field(self, obj):
        return obj.group.field


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_title',
        'image',
        'active',
        'created_at',
    ]

    def product_title(self, obj):
        return obj.product.title



@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'parent',
        'title',
        'slug',
        'is_private',
        'type_title',
        'active',
        'image_tag',
        'created_at',
    ]

    def image_tag(self, obj):
        if obj.image != '':
            return format_html('<img src="{}" style="width: 100px; height: 100px;" />'.format(obj.image.url))
        return ''

    def type_title(self, obj):
        return obj.collection_type.title


@admin.register(CollectionType)
class CollectionTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'active',
    ]


