# Generated by Django 3.2.5 on 2021-07-09 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210708_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
