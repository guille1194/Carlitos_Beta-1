# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Carlos_Home', '0004_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user_perfil',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
