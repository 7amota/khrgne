# Generated by Django 4.1.5 on 2023-02-15 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gellary',
            field=models.FileField(blank=True, null=True, upload_to='Photos/%y/%m/%d'),
        ),
    ]
