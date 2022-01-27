# Generated by Django 2.2.5 on 2022-01-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_index', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('addr', models.CharField(max_length=100)),
                ('pw', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='posting',
            table='Lender_Post',
        ),
    ]
