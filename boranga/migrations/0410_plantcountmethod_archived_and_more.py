# Generated by Django 5.0.8 on 2024-08-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0409_postfirehabitatinteraction_archived_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="plantcountmethod",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
