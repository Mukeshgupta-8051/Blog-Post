# Generated by Django 3.2.6 on 2021-08-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloger', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('post', models.CharField(max_length=255)),
            ],
        ),
    ]