# Generated by Django 4.2.4 on 2023-09-01 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_semester_remove_curator_decryptkey_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='CuratorID',
            new_name='Curator',
        ),
        migrations.RemoveField(
            model_name='curator',
            name='password',
        ),
    ]