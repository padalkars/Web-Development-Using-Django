# Generated by Django 2.0 on 2017-12-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20171213_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='descriptions',
            field=models.TextField(null='true'),
        ),
    ]
