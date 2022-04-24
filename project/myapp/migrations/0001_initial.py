# Generated by Django 4.0.1 on 2022-02-21 11:20

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=500)),
                ('emp_id', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('attendances', models.CharField(blank=True, choices=[('present', 'Present'), ('absent', 'Absent')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=500, unique=True)),
                ('gender', models.CharField(choices=[('MALE', '0'), ('FEMALE', '1')], max_length=10)),
                ('addres', models.CharField(max_length=500)),
                ('numbers', models.IntegerField()),
                ('photo', models.ImageField(upload_to='project/photo/')),
                ('degree', models.CharField(max_length=500)),
                ('institution', models.CharField(max_length=500)),
                ('acnumber', models.CharField(max_length=500)),
                ('branch', models.CharField(max_length=500)),
                ('ifsc', models.CharField(max_length=500)),
                ('emp_id', models.CharField(max_length=500, unique=True)),
                ('depaetment', models.CharField(max_length=500)),
                ('date_of_join', models.DateField()),
                ('position', models.CharField(max_length=500)),
                ('salary', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('active', '0'), ('inactive', '1')], max_length=50)),
                ('cv', models.FileField(upload_to='project/cv/')),
                ('bound', models.FileField(upload_to='project/bound/')),
                ('experience', models.CharField(default='NONE', editable=False, max_length=500)),
                ('company_name', models.CharField(default='NONE', max_length=500)),
                ('certificate', models.FileField(default='NONE', upload_to='project/certificate/')),
            ],
        ),
        migrations.CreateModel(
            name='user_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=500)),
                ('emp_id', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('msg', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('emp_id', models.CharField(max_length=500, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=500, unique=True)),
                ('addres', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('is_admin', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
