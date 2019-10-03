# Generated by Django 2.2.5 on 2019-10-02 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_auto_20191002_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='studentid',
        ),
        migrations.AddField(
            model_name='student',
            name='academicyear',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Academicyear'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Batch'),
        ),
    ]