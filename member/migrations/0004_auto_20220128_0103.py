# Generated by Django 2.2.5 on 2022-01-27 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20220127_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]