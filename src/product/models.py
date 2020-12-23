from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

from lib.basemodel import BaseModel


class Product(BaseModel):
    brand = models.ForeignKey("Brand", related_name='products',related_query_name="products", verbose_name=_(
        "Category"), on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='products',related_query_name="products" ,verbose_name=_(
        "Category"), on_delete=models.SET_NULL,null=True)
    name = models.CharField(_("name"), max_length=128)
    image = models.ImageField(_("image"), upload_to='product/images')
    details = models.TextField(verbose_name=_("detail"))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Product')

class Category(BaseModel):

    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    image = models.ImageField(_("image"), upload_to='category/images',null=True,blank=True)
    parent = models.ForeignKey(
        'self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True,
        related_name='children', related_query_name='children')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Cataegories')


class Brand(BaseModel):
    name = models.CharField(_("name"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    image = models.ImageField(_("image"), upload_to='brand/images')
    details = models.TextField(verbose_name=_("detail"))

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class Image(BaseModel):
    product=models.ForeignKey("Brand", related_name='posts', verbose_name=_(
        "Category"), on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='product/images')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Image')





