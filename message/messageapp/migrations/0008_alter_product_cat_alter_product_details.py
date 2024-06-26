# Generated by Django 5.0 on 2024-06-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0007_alter_product_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Small_Suv'), (2, 'Medium_Suv'), (3, 'Large_Suv')], verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=400, verbose_name='product details'),
        ),
    ]
