# Generated by Django 3.0.5 on 2020-04-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200420_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signup_confirmation',
            field=models.BooleanField(default=False),
        ),
    ]