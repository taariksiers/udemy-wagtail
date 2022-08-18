from django.db import models
from wagtail.snippets.models import register_snippet


@register_snippet
class Testimonial(models.Model):
    """
    Testimonial class
    """

    quote = models.TextField(max_length=500, blank=False, null=False)
    attribution = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        """
        :return: str
        """
        return f"{self.quote} by {self.attribution}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = f"{verbose_name}s"
