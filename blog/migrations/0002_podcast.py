# Generated by Django 3.1.4 on 2020-12-31 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embed', models.CharField(max_length=512, verbose_name='Vkládací kód')),
                ('published', models.DateTimeField(blank=True, verbose_name='Uveřejněno')),
            ],
        ),
    ]