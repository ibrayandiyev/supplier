# Generated by Django 2.2.6 on 2020-05-04 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_lock'),
        ('trolley', '0005_trolleyorderitem_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesoriesitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='trolleyorderitem',
            name='lock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Lock'),
        ),
    ]