# Generated by Django 2.2.6 on 2019-10-11 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_fee_fine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='admissionnumber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Student'),
        ),
    ]
