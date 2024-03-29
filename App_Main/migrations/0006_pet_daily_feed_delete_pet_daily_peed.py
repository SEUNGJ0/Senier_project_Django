# Generated by Django 4.1.1 on 2022-11-02 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Main', '0005_pet_info_alter_pet_daily_peed_pet_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet_daily_feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Daily_date', models.DateField(verbose_name='날짜')),
                ('Daily_feed', models.IntegerField(verbose_name='지급된 사료량')),
                ('Remain_feed', models.IntegerField(null=True, verbose_name='남은 사료량')),
                ('pet_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Main.pet_info')),
            ],
        ),
        migrations.DeleteModel(
            name='Pet_daily_peed',
        ),
    ]
