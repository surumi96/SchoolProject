# Generated by Django 2.2.5 on 2019-10-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20191001_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='standardid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]