# Generated by Django 3.2.9 on 2021-11-10 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0011_alter_link_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-id'], 'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
    ]