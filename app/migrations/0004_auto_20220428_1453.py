# Generated by Django 3.1.14 on 2022-04-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220427_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='customerPhone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='customerinfo',
            unique_together={('customerID', 'customerPhone')},
        ),
    ]
