# Generated by Django 4.1 on 2022-08-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginwebsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='session_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
