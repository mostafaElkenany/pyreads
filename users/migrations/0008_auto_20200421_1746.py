# Generated by Django 3.0.5 on 2020-04-21 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200421_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='featureing_date',
            new_name='featuring_date',
        ),
    ]
