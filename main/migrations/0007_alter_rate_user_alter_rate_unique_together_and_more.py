# Generated by Django 4.1.5 on 2023-02-14 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_rate_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('user', 'item')},
        ),
        migrations.AlterIndexTogether(
            name='rate',
            index_together={('user', 'item')},
        ),
    ]
