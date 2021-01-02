# Generated by Django 3.1.4 on 2020-12-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Titulek')),
                ('author', models.CharField(blank=True, max_length=256, verbose_name='Autor')),
                ('content', models.TextField(verbose_name='Obsah')),
                ('published', models.DateTimeField(blank=True, null=True, verbose_name='Uveřejněno')),
                ('modified', models.DateTimeField(blank=True, null=True, verbose_name='Upraveno')),
                ('draft', models.BooleanField(verbose_name='Je koncept?')),
                ('markdown', models.BooleanField(default=False, verbose_name='Používá Markdown?')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Článek',
                'verbose_name_plural': 'Články',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Nadpis')),
                ('content', models.TextField(verbose_name='Obsah')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Pořadové číslo')),
                ('markdown', models.BooleanField(default=False, verbose_name='Používá Markdown?')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Sekce',
                'verbose_name_plural': 'Sekce',
            },
        ),
    ]