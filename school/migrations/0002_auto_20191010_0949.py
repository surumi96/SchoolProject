# Generated by Django 2.2.6 on 2019-10-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]