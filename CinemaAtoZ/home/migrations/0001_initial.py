# Generated by Django 4.1.3 on 2022-11-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Rating', models.CharField(max_length=255)),
                ('Year', models.CharField(max_length=255)),
                ('Cast', models.CharField(max_length=255)),
            ],
        ),
    ]
