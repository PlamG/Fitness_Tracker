# Generated by Django 5.1.3 on 2024-12-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_appuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.PositiveIntegerField(),
        ),
    ]
