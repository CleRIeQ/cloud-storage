# Generated by Django 3.2.13 on 2022-05-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]