# Generated by Django 4.1.2 on 2022-12-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_alter_advert_phone_alter_advert_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='type',
            field=models.CharField(choices=[('find', 'найдено'), ('lost', 'потеряно')], max_length=200),
        ),
    ]