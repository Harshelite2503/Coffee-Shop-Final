# Generated by Django 3.1.14 on 2022-04-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220429_1434'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='waiter',
            constraint=models.CheckConstraint(check=models.Q(waiterID__gt=0), name='id2validation'),
        ),
    ]
