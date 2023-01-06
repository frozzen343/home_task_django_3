# Generated by Django 4.1.5 on 2023-01-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=50)),
                ('lte_exists', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
    ]