# Generated by Django 4.1 on 2022-12-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=150)),
                ('teacher_email', models.EmailField(max_length=254)),
                ('roll_number', models.IntegerField()),
            ],
        ),
    ]
