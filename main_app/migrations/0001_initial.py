# Generated by Django 3.1.3 on 2021-03-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('payment', models.CharField(max_length=20)),
            ],
        ),
    ]
