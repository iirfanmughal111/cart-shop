# Generated by Django 4.0.5 on 2022-06-10 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_blog_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_title', models.CharField(default='', max_length=100)),
                ('cat_slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='featured',
        ),
        migrations.AlterField(
            model_name='post',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
