# Generated by Django 2.1.6 on 2019-04-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_pending_user_borrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending',
            name='num_borrowed',
            field=models.CharField(max_length=255),
        ),
    ]
