# Generated by Django 4.1.13 on 2025-02-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('task_title', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('deadline', models.CharField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
