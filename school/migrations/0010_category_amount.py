# Generated by Django 2.2.6 on 2019-10-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20191017_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]