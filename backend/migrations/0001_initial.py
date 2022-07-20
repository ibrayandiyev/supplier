# Generated by Django 2.2.6 on 2020-04-28 05:56

import backend.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('cities_light', '0008_city_timezone'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('picture', models.ImageField(blank=True, upload_to=backend.models.content_file_user)),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('admin_user', 'Can use modules admin'), ('guest_user', 'Can use modules guest')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Castor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('b_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('b_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('worker', models.CharField(blank=True, max_length=100, null=True)),
                ('finished', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CsvArchivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=155, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=backend.models.csv_file)),
            ],
        ),
        migrations.CreateModel(
            name='DrawerColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('b_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WallType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('b_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StockFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.TextField(blank=True)),
                ('min_quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('max_quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('less', models.CharField(blank=True, max_length=10, null=True)),
                ('greater', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('picture', models.ImageField(blank=True, upload_to=backend.models.content_file_stock)),
                ('reference', models.TextField(blank=True, unique=True)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('minium', models.IntegerField(blank=True, default=1, null=True)),
                ('b_group', models.IntegerField(blank=True, default=0, null=True)),
                ('pdf', models.FileField(blank=True, upload_to=backend.models.content_file_stock_pdf)),
                ('location', models.TextField(blank=True)),
                ('width', models.IntegerField(blank=True, default=1, null=True)),
                ('height', models.IntegerField(blank=True, default=1, null=True)),
                ('depth', models.IntegerField(blank=True, default=1, null=True)),
                ('weight', models.IntegerField(blank=True, default=1, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to='backend.Stock')),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_item', to='backend.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='GroupFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.TextField(blank=True)),
                ('min_quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('max_quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('less', models.CharField(blank=True, max_length=10, null=True)),
                ('greater', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('country', models.TextField(blank=True)),
                ('owner', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('picture', models.ImageField(blank=True, upload_to=backend.models.content_file_contact)),
                ('telephone', models.CharField(blank=True, max_length=250, null=True)),
                ('mobile', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('web', models.CharField(blank=True, max_length=250, null=True)),
                ('notes', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('pdf', models.FileField(blank=True, upload_to=backend.models.content_file_contact_pdf)),
                ('products', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.Country')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='backend.Contact')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CommandWorkerHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('command', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Command')),
            ],
        ),
        migrations.CreateModel(
            name='CommandFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.TextField(blank=True)),
                ('worker', models.TextField(blank=True)),
                ('min_quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('max_quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('in_progress', models.CharField(blank=True, max_length=10, null=True)),
                ('finished', models.CharField(blank=True, max_length=10, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='command', to='backend.Stock'),
        ),
        migrations.AddField(
            model_name='command',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ClientFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('country', models.TextField(blank=True)),
                ('owner', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('picture', models.ImageField(blank=True, upload_to=backend.models.content_file_contact)),
                ('telephone', models.CharField(blank=True, max_length=250, null=True)),
                ('mobile', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('web', models.CharField(blank=True, max_length=250, null=True)),
                ('notes', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('pdf', models.FileField(blank=True, upload_to=backend.models.content_file_contact_pdf)),
                ('products', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.Country')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='backend.Client')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BoxFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.TextField(blank=True)),
                ('min_quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('max_quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('less', models.CharField(blank=True, max_length=10, null=True)),
                ('greater', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]