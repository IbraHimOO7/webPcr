# Generated by Django 3.1.3 on 2021-02-24 20:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman', '0010_auto_20210223_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='lamanAtas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kataUtama', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('brosur', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
