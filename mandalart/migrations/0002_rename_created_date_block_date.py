# Generated by Django 3.2 on 2021-08-12 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandalart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='created_date',
            new_name='date',
        ),
    ]
