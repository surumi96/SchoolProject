# Generated by Django 2.2.6 on 2019-11-05 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0030_auto_20191105_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeallocation',
            name='admission',
        ),
    ]
