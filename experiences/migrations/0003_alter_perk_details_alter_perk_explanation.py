# Generated by Django 5.0.1 on 2024-01-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perk',
            name='details',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='perk',
            name='explanation',
            field=models.TextField(blank=True, default=''),
        ),
    ]