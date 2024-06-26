# Generated by Django 5.0 on 2024-01-16 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('details', models.CharField(max_length=100)),
                ('cat', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='msg',
        ),
    ]
