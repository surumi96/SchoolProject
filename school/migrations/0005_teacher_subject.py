# Generated by Django 2.2.5 on 2019-09-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]