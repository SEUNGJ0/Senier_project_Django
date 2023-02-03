# Generated by Django 4.1.1 on 2022-10-27 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=100)),
                ('pet_birth', models.DateField()),
                ('pet_weight', models.DecimalField(decimal_places=5, max_digits=1000)),
                ('pet_breed', models.CharField(max_length=100)),
                ('pet_diet', models.IntegerField()),
                ('pet_feed_time_B', models.TimeField()),
                ('pet_feed_time_L', models.TimeField()),
                ('pet_feed_time_D', models.TimeField()),
                ('pet_feed_amount', models.IntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
