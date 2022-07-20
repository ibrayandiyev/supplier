# Generated by Django 2.2.6 on 2020-05-05 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_lock'),
        ('timesheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskitem',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Stock'),
        ),
    ]
