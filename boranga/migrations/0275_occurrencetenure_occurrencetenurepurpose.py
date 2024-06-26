# Generated by Django 3.2.25 on 2024-06-04 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0274_auto_20240531_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccurrenceTenurePurpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OccurrenceTenure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('current', 'Current'), ('historical', 'Historical')], default='current', max_length=100)),
                ('tenure_area_id', models.CharField(blank=True, max_length=100, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=255, null=True)),
                ('owner_count', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('significant_to_occurrence', models.BooleanField(blank=True, default=False, null=True)),
                ('occurrence_geometry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occurrence_tenures', to='boranga.occurrencegeometry')),
                ('purpose', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='occurrence_tenures', to='boranga.occurrencetenurepurpose')),
            ],
            options={
                'unique_together': {('occurrence_geometry', 'tenure_area_id')},
            },
        ),
    ]
