# Generated by Django 2.1.7 on 2019-04-01 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_save'),
    ]

    operations = [
        migrations.RenameField(
            model_name='save',
            old_name='statement',
            new_name='json_field',
        ),
    ]
