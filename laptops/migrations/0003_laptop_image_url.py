# Generated by Django 3.0.8 on 2020-07-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0002_laptop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
