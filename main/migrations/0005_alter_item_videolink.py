# Generated by Django 4.1.5 on 2023-02-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_item_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='videolink',
            field=models.URLField(blank=True, max_length=800, null=True),
        ),
    ]
