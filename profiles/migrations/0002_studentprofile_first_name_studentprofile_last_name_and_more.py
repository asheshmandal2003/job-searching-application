# Generated by Django 5.1.3 on 2024-12-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='first_name',
            field=models.CharField(default='First Name', max_length=100),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=100),
        ),
        migrations.AddField(
            model_name='tpoprofile',
            name='first_name',
            field=models.CharField(default='First Name', max_length=100),
        ),
        migrations.AddField(
            model_name='tpoprofile',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=100),
        ),
    ]
