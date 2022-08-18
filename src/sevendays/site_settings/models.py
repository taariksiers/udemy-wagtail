from lib2to3.pytree import Base
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSetting(BaseSetting):
    instagram = models.URLField(max_length=256)
    panels = [
        FieldPanel("instagram")
    ]
