# Generated by Django 4.0.5 on 2022-07-09 07:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hablemosapp', '0008_alter_debate_creado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='creado',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
