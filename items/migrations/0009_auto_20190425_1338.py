# Generated by Django 2.1.6 on 2019-04-25 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0008_pending_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='borrow',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
