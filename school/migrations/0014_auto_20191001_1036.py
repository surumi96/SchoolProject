# Generated by Django 2.2.5 on 2019-10-01 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Standard'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Periods'),
        ),
    ]
