# Generated by Django 4.1.2 on 2022-12-24 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_alter_advert_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='name',
        ),
    ]
