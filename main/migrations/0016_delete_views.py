# Generated by Django 4.1.5 on 2023-02-15 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_item_id_alter_rate_id_alter_views_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Views',
        ),
    ]
