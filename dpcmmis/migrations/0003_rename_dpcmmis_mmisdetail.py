# Generated by Django 4.0.3 on 2022-03-16 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpcmmis', '0002_rename_userdata_dpcmmis'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dpcmmis',
            new_name='mmisdetail',
        ),
    ]