# Generated by Django 3.1.2 on 2020-10-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20201009_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='_id',
            field=models.CharField(blank=True, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='_id',
            field=models.CharField(blank=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]