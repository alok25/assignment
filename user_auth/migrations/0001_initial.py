# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=80, null=True, blank=True)),
                ('last_name', models.CharField(max_length=80, null=True, blank=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(default=b'User', max_length=50, null=True, choices=[(b'Admin', b'ADMIN'), (b'User', b'USER')])),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OTPGenerator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('otp_number', models.IntegerField(null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('expiry_time', models.DateTimeField(default=user_auth.models.get_otp_expirity)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'otp_generator',
            },
        ),
    ]
