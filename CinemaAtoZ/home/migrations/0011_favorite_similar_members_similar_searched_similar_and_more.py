# Generated by Django 4.1.3 on 2022-11-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_favorite_cast_alter_favorite_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='similar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='similar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='searched',
            name='similar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='watched',
            name='similar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='similar',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
