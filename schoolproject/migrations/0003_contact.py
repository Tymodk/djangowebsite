# Generated by Django 2.0.1 on 2018-01-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolproject', '0002_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('adres', models.CharField(max_length=100)),
                ('telenummer', models.CharField(max_length=100)),
                ('inhoud', models.CharField(max_length=5000)),
            ],
        ),
    ]
