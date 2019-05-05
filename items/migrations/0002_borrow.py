# Generated by Django 2.1.7 on 2019-04-17 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(max_length=25)),
                ('item', models.ManyToManyField(to='items.Item')),
            ],
        ),
    ]