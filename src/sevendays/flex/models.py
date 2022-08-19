from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks


class FlexPage(Page):

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
        # ("richtext_with_title", blocks.RichTextWithTitleBlock()),
        ("richtext", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
            features=["bold", "italic", "ol", "ul", "link"]
        )),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = f"{verbose_name}s"
