# Generated by Django 4.1.3 on 2022-12-07 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0004_alter_people_homeworld'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.PROTECT, to='ex09.planets'),
        ),
    ]
