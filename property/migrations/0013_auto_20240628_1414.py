# Generated by Django 2.2.24 on 2024-06-28 11:14

from django.db import migrations
import phonenumbers


def fill_owners_pure_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        if phonenumbers.is_valid_number(flat.owners_phonenumber):
            flat.owner_pure_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0012_auto_20240628_1407'),
    ]

    operations = [
    ]