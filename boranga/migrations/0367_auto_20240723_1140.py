# Generated by Django 3.2.25 on 2024-07-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0366_merge_0365_auto_20240722_1043_0365_auto_20240722_1335"),
    ]

    operations = [
        migrations.AddField(
            model_name="committee",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]