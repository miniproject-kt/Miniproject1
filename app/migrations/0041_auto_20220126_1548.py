# Generated by Django 2.2.5 on 2022-01-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_auto_20220126_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='pw',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
