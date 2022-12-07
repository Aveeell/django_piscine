# Generated by Django 4.1.3 on 2022-12-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('title', models.CharField(max_length=64, unique=True)),
                ('episode_nb', models.IntegerField(primary_key=True, serialize=False)),
                ('opening_crawl', models.TextField()),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
