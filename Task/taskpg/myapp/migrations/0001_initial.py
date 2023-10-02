# Generated by Django 4.2.5 on 2023-10-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
