# Generated by Django 2.2.6 on 2019-11-08 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0032_feecollection_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feecollection',
            name='fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='school.Feecategory'),
        ),
    ]