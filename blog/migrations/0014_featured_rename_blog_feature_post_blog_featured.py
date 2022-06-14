# Generated by Django 4.0.5 on 2022-06-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rename_blog_featured_post_blog_feature_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='featured',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_title', models.CharField(default='', max_length=100)),
                ('f_desc', models.CharField(default='', max_length=10000)),
                ('f_category', models.CharField(default='', max_length=50)),
                ('f_pub_date', models.DateField(auto_now_add=True)),
                ('f_imgs', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='blog_feature',
            new_name='blog_featured',
        ),
    ]
