# Generated by Django 2.2.5 on 2022-01-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220125_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
    ]