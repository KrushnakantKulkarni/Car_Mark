# Generated by Django 5.0 on 2024-01-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
