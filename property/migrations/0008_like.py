# Generated by Django 2.2.24 on 2024-06-28 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0007_complaint_flat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dislike', models.BooleanField(default=False)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Квартира, которую лайнули')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats_likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул?')),
            ],
        ),
    ]
