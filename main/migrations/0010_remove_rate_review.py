# Generated by Django 4.1.5 on 2023-02-14 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rate_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='review',
        ),
    ]
