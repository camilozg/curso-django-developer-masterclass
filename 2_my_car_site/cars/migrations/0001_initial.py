# Generated by Django 4.1.3 on 2022-12-15 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beand', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
