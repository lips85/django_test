# Generated by Django 5.0.1 on 2024-01-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_rename_price_house_price_per_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='pet_allowed',
            field=models.BooleanField(default=True),
        ),
    ]
