# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 07:33
from __future__ import unicode_literals

from django.db import migrations, models
import user_auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=80, null=True)),
                ('last_name', models.CharField(blank=True, max_length=80, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(choices=[(b'Admin', b'ADMIN'), (b'User', b'USER')], default=b'User', max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OTPGenerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_number', models.IntegerField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('expiry_time', models.DateTimeField(default=user_auth.models.get_otp_expirity)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'otp_generator',
            },
        ),
    ]
