# Generated by Django 3.0.14 on 2022-12-16 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=12)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Guardias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=12)),
                ('activo', models.BooleanField()),
                ('foto', models.ImageField(upload_to='fotos')),
                ('empresas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Empresa')),
            ],
        ),
    ]
