# Generated by Django 2.2.6 on 2020-05-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='nif',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
