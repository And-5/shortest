# Generated by Django 3.2.9 on 2021-11-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0007_alter_link_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]