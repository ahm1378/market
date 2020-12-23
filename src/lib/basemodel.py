from django.db import models
from django.utils.translation import ugettext_lazy as _




class BaseModel(models.Model):
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        abstract = True
