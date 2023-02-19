# Generated by Django 4.1.5 on 2023-02-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_delete_fav'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='views',
            name='view',
        ),
        migrations.AddConstraint(
            model_name='views',
            constraint=models.UniqueConstraint(fields=('user', 'item'), name='name of constraint'),
        ),
    ]
