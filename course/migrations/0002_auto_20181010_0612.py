# Generated by Django 2.1.2 on 2018-10-10 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='desription',
            new_name='description',
        ),
    ]
