# Generated by Django 3.2.12 on 2022-04-02 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlparser', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RawZip',
            new_name='RawArchive',
        ),
    ]
