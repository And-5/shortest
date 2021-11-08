# Generated by Django 3.2.9 on 2021-11-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0006_link_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.URLField(error_messages={'unique': 'User with this email already exists.'}, max_length=1000, unique=True),
        ),
    ]
