# Generated by Django 4.0.4 on 2022-06-02 14:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='message',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
