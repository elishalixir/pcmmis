# Generated by Django 4.0.6 on 2022-09-03 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpcmmis', '0003_alter_asgmelisha_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asgmelisha',
            name='eight',
        ),
        migrations.RemoveField(
            model_name='asgmelisha',
            name='five',
        ),
        migrations.RemoveField(
            model_name='asgmelisha',
            name='seven',
        ),
        migrations.RemoveField(
            model_name='asgmelisha',
            name='six',
        ),
    ]
