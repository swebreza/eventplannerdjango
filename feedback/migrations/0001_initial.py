# Generated by Django 4.0.4 on 2022-06-02 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
