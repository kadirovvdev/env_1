# Generated by Django 5.0.4 on 2024-05-01 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Phone',
            new_name='Products',
        ),
    ]