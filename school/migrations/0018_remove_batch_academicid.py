# Generated by Django 2.2.5 on 2019-10-01 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_auto_20191001_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='academicid',
        ),
    ]
