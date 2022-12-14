# Generated by Django 4.1.3 on 2022-12-07 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('climate', models.TextField()),
                ('diameter', models.IntegerField()),
                ('orbital_period', models.IntegerField()),
                ('population', models.BigIntegerField()),
                ('rotation_period', models.IntegerField()),
                ('surface', models.FloatField()),
                ('terrain', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('birth_year', models.CharField(max_length=32)),
                ('gender', models.CharField(max_length=32)),
                ('eye_color', models.CharField(max_length=32)),
                ('hair_color', models.CharField(max_length=32)),
                ('height', models.IntegerField()),
                ('mass', models.FloatField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('homeworld', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ex09.planets')),
            ],
        ),
    ]
