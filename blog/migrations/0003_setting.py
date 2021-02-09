# Generated by Django 3.1.4 on 2021-02-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210103_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Jméno k zobrazení')),
                ('key', models.CharField(max_length=256, unique=True, verbose_name='Klíč')),
                ('value', models.TextField(blank=True, verbose_name='Hodnota')),
            ],
            options={
                'verbose_name': 'Nastavení',
                'verbose_name_plural': 'Nastavení',
            },
        ),
    ]