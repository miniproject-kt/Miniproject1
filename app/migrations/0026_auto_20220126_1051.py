# Generated by Django 2.2.5 on 2022-01-26 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20220126_1047'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='borrower',
            table='Borrower_Post',
        ),
        migrations.AlterModelTable(
            name='borrower_chatting',
            table='Borrower_Chatting',
        ),
        migrations.AlterModelTable(
            name='lender',
            table='Lender_Post',
        ),
        migrations.AlterModelTable(
            name='lender_chatting',
            table='Lender_Chatting',
        ),
        migrations.AlterModelTable(
            name='object',
            table='Object',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]