# Generated by Django 3.2.12 on 2022-08-04 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelmanager', '0007_auto_20220804_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mlmodel',
            old_name='model_version',
            new_name='version',
        ),
    ]