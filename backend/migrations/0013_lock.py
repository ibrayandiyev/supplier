# Generated by Django 2.2.6 on 2020-05-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_strip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('b_deleted', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]