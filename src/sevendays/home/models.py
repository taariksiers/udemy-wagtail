from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks


class HomePage(Page):
    banner_title = models.CharField(max_length=100, default="Welcome to my home page")
    lead_text = models.CharField(max_length=140, blank=True, help_text="sub heading under the banner")
    button = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="Select an optional page to link to",
        on_delete=models.SET_NULL
    )
    button_text = models.CharField(
        max_length=50,
        default="Read More",
        blank=False,
        help_text="Button text"
    )
    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL
    )

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonials", SnippetChooserBlock(
            target_model="testimonials.Testimonial",
            template="streams/testimonial_block.html")
         ),
        ("pricing_table", blocks.PricingTableBlock()),
    ], null=True, blank=True)
    # blank=True you can save the homepage without any input for this
    # null=True - allowed by DB

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        FieldPanel("banner_title"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel("body"),
    ]
