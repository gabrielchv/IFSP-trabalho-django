# Generated by Django 4.1 on 2022-11-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginwebsite', '0003_remove_user_datecreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]
