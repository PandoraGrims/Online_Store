# Generated by Django 4.2.2 on 2023-07-03 22:04

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_good_remainder_alter_good_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('7777777.99'))]),
        ),
    ]
