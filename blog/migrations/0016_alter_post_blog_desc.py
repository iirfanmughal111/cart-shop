# Generated by Django 4.0.5 on 2022-06-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_delete_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_desc',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
