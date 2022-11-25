# Generated by Django 4.1.3 on 2022-11-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_members_duration_members_imdb_rating_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Rating', models.CharField(max_length=255)),
                ('Year', models.CharField(max_length=255)),
                ('IMDb_Rating', models.CharField(max_length=255, null=True)),
                ('Rott_Rating', models.CharField(max_length=255, null=True)),
                ('Meta_Rating', models.CharField(max_length=255, null=True)),
                ('Cast', models.CharField(max_length=255)),
                ('Duration', models.CharField(max_length=255, null=True)),
                ('Plot', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
