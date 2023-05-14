# Generated by Django 4.1.5 on 2023-02-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_fav_remove_views_name of constraint_views_view_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='fav',
            name='fav',
        ),
        migrations.AddConstraint(
            model_name='fav',
            constraint=models.UniqueConstraint(fields=('usera', 'item'), name='fav'),
        ),
    ]