# Generated by Django 4.2.7 on 2024-01-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0009_location_latitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='mqtterror',
            name='ip_address',
            field=models.CharField(blank=0, default=0, max_length=16, null=0),
        ),
    ]
