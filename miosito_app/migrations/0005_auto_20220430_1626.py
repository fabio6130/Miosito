# Generated by Django 2.2.24 on 2022-04-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miosito_app', '0004_auto_20220430_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devtools',
            name='frontend',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='languages',
            name='frontend',
            field=models.BooleanField(default=False),
        ),
    ]
