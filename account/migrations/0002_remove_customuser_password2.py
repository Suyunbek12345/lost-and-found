# Generated by Django 4.1.2 on 2022-12-04 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password2',
        ),
    ]
