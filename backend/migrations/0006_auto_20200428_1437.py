# Generated by Django 2.2.6 on 2020-04-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200428_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='width',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
