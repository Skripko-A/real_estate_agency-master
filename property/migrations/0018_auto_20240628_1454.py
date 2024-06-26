# Generated by Django 2.2.24 on 2024-06-28 11:54

from django.db import migrations


def connect_owners_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator(chunk_size=2000):
        owner, created = Owner.objects.get_or_create(full_name=flat.owner, defaults={'phone_number': flat.owners_phonenumber,
                                                                                     'pure_phone': flat.owner_pure_phonenumber})
        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20240628_1454'),
    ]

    operations = [
        migrations.RunPython(connect_owners_flats)
    ]
