# Generated by Django 4.0.5 on 2022-07-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hablemosapp', '0017_alter_debate_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='imagen'),
        ),
    ]