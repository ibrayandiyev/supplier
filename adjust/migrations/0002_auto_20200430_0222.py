# Generated by Django 2.2.6 on 2020-04-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adjust', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjustitem',
            name='adjust_qt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adjustitem',
            name='current_qt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adjustitem',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
