# Generated by Django 3.2.25 on 2024-07-31 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0382_auto_20240731_1041"),
    ]

    operations = [
        migrations.AddField(
            model_name="coordinatesource",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]