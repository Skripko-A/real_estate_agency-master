# Generated by Django 2.2.24 on 2024-06-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Новостройка?'),
        ),
    ]
