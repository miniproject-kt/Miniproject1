# Generated by Django 2.2.5 on 2022-01-26 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20220126_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower_chatting',
            name='borrower_index',
        ),
        migrations.RemoveField(
            model_name='borrower_chatting',
            name='posting_index',
        ),
        migrations.RemoveField(
            model_name='lender',
            name='lender_index',
        ),
        migrations.RemoveField(
            model_name='lender_chatting',
            name='lender_index',
        ),
        migrations.RemoveField(
            model_name='lender_chatting',
            name='posting_index',
        ),
        migrations.RemoveField(
            model_name='object',
            name='posting_index',
        ),
        migrations.DeleteModel(
            name='Borrower',
        ),
        migrations.DeleteModel(
            name='Borrower_Chatting',
        ),
        migrations.DeleteModel(
            name='Lender',
        ),
        migrations.DeleteModel(
            name='Lender_Chatting',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]