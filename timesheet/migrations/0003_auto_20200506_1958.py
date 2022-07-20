# Generated by Django 2.2.6 on 2020-05-06 11:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_lock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timesheet', '0002_taskitem_stock'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='TimeSheet',
        ),
        migrations.RenameModel(
            old_name='TaskFavorite',
            new_name='TimeSheetFavorite',
        ),
        migrations.RenameModel(
            old_name='TaskItem',
            new_name='TimeSheetItem',
        ),
        migrations.AlterModelOptions(
            name='timesheetitem',
            options={'ordering': ['start_time', 'end_time']},
        ),
        migrations.RenameField(
            model_name='timesheetitem',
            old_name='task',
            new_name='timesheet',
        ),
    ]
