# Generated by Django 2.0.7 on 2018-07-05 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180705_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_logout',
            field=models.DateTimeField(null=True),
        ),
    ]
