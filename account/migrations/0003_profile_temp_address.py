# Generated by Django 2.1.7 on 2019-03-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190302_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='temp_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
