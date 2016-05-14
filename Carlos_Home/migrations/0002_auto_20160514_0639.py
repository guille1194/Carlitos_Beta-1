# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Carlos_Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('orden', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('post_imagen', models.ImageField(upload_to='post_imagen/')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_video', models.CharField(max_length=300, null=True)),
                ('categorias', models.ForeignKey(to='Carlos_Home.Categoria')),
            ],
        ),
        migrations.AlterField(
            model_name='paciente',
            name='genero',
            field=models.CharField(max_length=1),
        ),
    ]
