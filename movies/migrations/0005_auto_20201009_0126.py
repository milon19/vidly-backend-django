# Generated by Django 3.1.2 on 2020-10-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20201009_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='_id',
            field=models.CharField(auto_created=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]
