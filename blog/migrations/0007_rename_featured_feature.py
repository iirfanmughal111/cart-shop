# Generated by Django 4.0.5 on 2022-06-10 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_featured'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='featured',
            new_name='feature',
        ),
    ]
