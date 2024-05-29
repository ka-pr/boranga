# Generated by Django 3.2.25 on 2024-05-28 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0261_merge_20240524_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_path', models.CharField(max_length=255)),
                ('proxy_url', models.CharField(max_length=255)),
                ('basic_auth_enabled', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('disabled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Proxy',
                'verbose_name_plural': 'Proxies',
                'ordering': ['request_path'],
            },
        ),
    ]