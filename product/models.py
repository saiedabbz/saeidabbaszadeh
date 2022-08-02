from pyexpat import model
from django.db import models

from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(_("title"), max_length=64)
    slug = models.SlugField(_("slug"))
    description = models.TextField(_("description"), null=True, blank=True)
    collections = models.ManyToManyField("product.Collection", verbose_name=_("collections"), related_name='products')
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    theme = models.CharField(_("Theme"), max_length=64, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class Showcase(models.Model):
    title = models.CharField(_("title"), max_length=64, null=True, blank=True)
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE, related_name="showcases")
    description = models.TextField(_("description"), null=True, blank=True)
    image = models.ImageField(_("image"), upload_to='showcases/')
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Showcase')
        verbose_name_plural = _('Showcases')
    
class ProductVariant(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE, related_name="variants")
    is_main = models.BooleanField(_("is main"), default=False)
    stock = models.BigIntegerField(_("stock"), default=0)
    price = models.BigIntegerField(_("price"))
    options = models.ManyToManyField("product.ProductOption", verbose_name=_("options"))
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return  f"{self.product.title} - {list(self.options.all().values_list('value', flat=True))}"

    class Meta:
        verbose_name = _('Product Variant')
        verbose_name_plural = _('Product Variants')

class ProductOptionGroup(models.Model):
    field = models.CharField(_("field"), max_length=64)
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.field

    class Meta:
        verbose_name = _('Product Option Group')
        verbose_name_plural = _('Product Option Groups')

class ProductOption(models.Model):
    group = models.ForeignKey("product.ProductOptionGroup", verbose_name=_("field"), on_delete=models.CASCADE)
    value = models.CharField(_("value"), max_length=128)
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.group.field} - {self.value}"

    class Meta:
        verbose_name = _('Product Option')
        verbose_name_plural = _('Product Options')

class ProductImage(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE, related_name="images")
    title = models.CharField(_("title"), max_length=200, blank=True, null=True)
    image = models.ImageField(_("image"), upload_to='products/')
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')

class ProductExtra(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE, related_name="extras")
    title = models.CharField(_("title"), max_length=200, blank=True, null=True)
    desc = models.TextField(_("desc"), default='')
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _('Product Extra')
        verbose_name_plural = _('Product Extras')

class Collection(models.Model):
    title = models.CharField(_("title"), max_length=64)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(_("slug"))
    collection_type = models.ForeignKey("product.CollectionType", verbose_name=_("collection type"), on_delete=models.CASCADE)
    is_private = models.BooleanField(_("is private"), default=False)
    image = models.ImageField(_("image"), upload_to='collections/', null=True, blank=True)
    active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    theme = models.CharField(_("Theme"), max_length=64, null=True, blank=True)

    

    def __str__(self):
        if self.parent_id is not None:
            return f"{self.parent} -> {self.title}"
        else:
            return self.title

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')


class CollectionType(models.Model):
    title = models.CharField(_("title"), max_length=64)
    active = models.BooleanField(_("active"), default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Collection Type')
        verbose_name_plural = _('Collection Types')


