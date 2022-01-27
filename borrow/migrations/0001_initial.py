# Generated by Django 2.2.5 on 2022-01-25 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrow.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrow.Member')),
                ('stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrow.Stuff')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrow.Member')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrow.Post')),
            ],
        ),
    ]