# Generated by Django 5.0.2 on 2024-02-08 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='anime',
            name='format',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='animes.format'),
        ),
    ]