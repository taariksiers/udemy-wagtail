# Generated by Django 4.0.6 on 2022-08-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='Welcome to my home page', max_length=100),
        ),
    ]
