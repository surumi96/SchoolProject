# Generated by Django 2.2.5 on 2019-10-02 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_auto_20191002_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='studentid',
        ),
        migrations.AddField(
            model_name='batch',
            name='studentid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='school.Student'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='isactive',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
