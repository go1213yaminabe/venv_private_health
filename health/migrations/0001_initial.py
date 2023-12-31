# Generated by Django 3.2.7 on 2023-06-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning_state', models.TextField(blank=True, null=True, verbose_name='朝の症状')),
                ('morning_temperature', models.IntegerField(blank=True, null=True, verbose_name='朝の体温')),
                ('night_state', models.TextField(blank=True, null=True, verbose_name='夜の症状')),
                ('night_temperature', models.IntegerField(blank=True, null=True, verbose_name='夜の体温')),
                ('note', models.TextField(blank=True, null=True, verbose_name='備考')),
                ('niti', models.DateTimeField(blank=True, null=True, verbose_name='作成日時')),
            ],
            options={
                'verbose_name_plural': 'health',
            },
        ),
    ]
