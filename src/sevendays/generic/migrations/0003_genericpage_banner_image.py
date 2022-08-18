# Generated by Django 4.0.6 on 2022-08-11 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('generic', '0002_genericpage_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
