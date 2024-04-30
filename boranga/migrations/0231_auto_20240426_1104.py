# Generated by Django 3.2.25 on 2024-04-26 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0230_auto_20240423_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='occconservationthreat',
            name='occurrence_report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='original_report', to='boranga.occurrencereport'),
        ),
        migrations.AlterField(
            model_name='occurrencereportdeclineddetails',
            name='occurrence_report',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='declined_details', to='boranga.occurrencereport'),
        ),
    ]