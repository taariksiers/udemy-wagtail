from django import forms
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.StructBlock):

    text = blocks.CharBlock(
        required=True,
        help_text="Text to display"
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"


class LinkValue(blocks.StructValue):

    def url(self):
        """
        :return:
        """
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        return internal_page or external_link or ""


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(max_length=50, default="More details")
    internal_page = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        value_class = LinkValue


class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text="Bold title text for this card. Max length of 100 characters")
    text = blocks.TextBlock(
        max_length=255,
        help_text="Optional text for this card. Max length of 255 characters.",
        required=False)
    image = ImageChooserBlock(help_text="Image will be automagically cropped to 570px 370px")
    link = Link(help_text="Enter a link or select a page")


class CardsBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Stack of Cards"
        help_text = "List of Centered text to display on the page"


class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )


class ImageAndTextBlock(blocks.StructBlock):

    image = ImageChooserBlock(help_text="Automagically cropped to 786px by 552px")
    image_alignment = RadioSelectBlock(
        choices=(
            ("left", "Image to the left"),
            ("right", "Image to the right")
        ),
        default="left",
        help_text="Image position with text on opposite side"
    )
    title = blocks.CharBlock(max_length=60, help_text="Max length of 60 characters.")
    text = blocks.CharBlock(max_length=140, required=False)
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"


class CallToActionBlock(blocks.StructBlock):

    title = blocks.CharBlock(max_length=200, help_text="Max length of 200 Characters.")
    link = Link()

    class Meta:
        template = "streams/call_to_action_block.html"  # without this line it renders directly to main template
        icon = "plus"
        label = "Call to Action"


class PricingTableBlock(TableBlock):

    class Meta:
        template = "streams/pricing_table_block.html"
        label = "Pricing Table"
        icon = "table"
        help_text = "Pricing Table should have 4 columns."


class RichTextWithTitleBlock(blocks.StructBlock):

    title = blocks.CharBlock(max_length=50)
    context = blocks.RichTextBlock(features=[])

    class Meta:
        template = "streams/simple_richtext_block.html"
        label = "Rich Text Title Block"
        icon = "title"
        help_text = "Rich text for title block"
