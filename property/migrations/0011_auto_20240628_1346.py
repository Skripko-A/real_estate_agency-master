# Generated by Django 2.2.24 on 2024-06-28 10:46

from django.db import migrations
import phonenumbers


def fill_owners_pure_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        flat.owner_pure_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20240628_1333'),
    ]

    operations = [
        migrations.RunPython(fill_owners_pure_numbers)
    ]