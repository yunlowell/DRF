# Generated by Django 4.2 on 2024-09-09 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='1990-01-01'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='닉네임을 설정해주세요', max_length=10, unique=True),
        ),
    ]
