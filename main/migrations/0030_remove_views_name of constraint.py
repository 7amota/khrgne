# Generated by Django 4.1.5 on 2023-02-15 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_remove_views_view_views_name of constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='views',
            name='name of constraint',
        ),
    ]