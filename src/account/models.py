from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from lib.basemodel import BaseModel
from product.models import Product


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    first_name= models.CharField(_('display name'), max_length=150,blank=True,null=True)
    last_name = models.CharField(_('display name'), max_length=150, blank=True, null=True)
    mobile = models.CharField(_('display name'), max_length=150)
    image=models.ImageField(_("avatar"), upload_to='user/avatars', blank=True)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class Comment(BaseModel):
    product= models.ForeignKey(Product, related_name='comments', related_query_name='comments', verbose_name=_(
        "product"), on_delete=models.CASCADE)
    content = models.TextField(_("Content"))
    rate=models.SmallIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        "User"), on_delete=models.CASCADE)


class Adress(BaseModel):
    city = models.CharField(_('city'), max_length=150)
    street = models.CharField(_('street'), max_length=150)
    allay = models.CharField(_('display name'), max_length=150, blank=True, null=True)
    zip_code = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"),
                               related_name='adresses', related_query_name='adreses',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('adress')


class Shop(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        "user"), on_delete=models.CASCADE)
    name = models.CharField(_('street'), max_length=150)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    dicription=models.TextField(_("discription"))
    image = models.ImageField(_("avatar"), upload_to='shop/images', blank=True)

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')

class ShopProduct(BaseModel):
    shop=models.ForeignKey(Shop,verbose_name=_("shop"),on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    price=models.IntegerField(_("price"))
    quantity=models.SmallIntegerField(_("quantity"))

    class Meta:
        verbose_name = _('shpproduct')
        verbose_name_plural = _('shopProducts')


class Email(BaseModel):
    subject = models.CharField(_('subject'), max_length=250)
    content = models.TextField(_("Content"))
    user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name="emails",related_query_name="emails",verbose_name=_(
        "user"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('email')
