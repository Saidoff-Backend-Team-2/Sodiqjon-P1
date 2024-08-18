from django.db import models
from common.models import Media
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """Products' data"""
    title = models.CharField(_('title'), max_length=150)
    desc = models.TextField(_('decription'))
    size = models.CharField(_('volume'), max_length=25, help_text="in liters")
    image = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} - {self.size} l'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductAttribute(models.Model):
    """Products Attributes"""
    name = models.CharField(_('attribute name'), max_length=100)
    value = models.PositiveSmallIntegerField(_('attribute value'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.value}'

    class Meta:
        verbose_name = 'Product Attribute'
        verbose_name_plural = 'Product Attributes'
