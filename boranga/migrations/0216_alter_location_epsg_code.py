# Generated by Django 3.2.25 on 2024-04-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0215_location_epsg_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='epsg_code',
            field=models.IntegerField(default=4326),
        ),
    ]
