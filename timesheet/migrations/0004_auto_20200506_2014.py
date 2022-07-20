# Generated by Django 2.2.6 on 2020-05-06 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_task'),
        ('timesheet', '0003_auto_20200506_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheetitem',
            name='name',
        ),
        migrations.AddField(
            model_name='timesheetitem',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Task'),
        ),
    ]
