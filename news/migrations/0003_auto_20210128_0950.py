# Generated by Django 3.1.1 on 2021-01-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210120_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_by',
            field=models.CharField(blank=True, max_length=200, verbose_name='Published By'),
        ),
    ]
