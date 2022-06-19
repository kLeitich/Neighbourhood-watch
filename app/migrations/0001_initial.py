# Generated by Django 4.0.5 on 2022-06-19 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('ppic', models.ImageField(upload_to='ppic')),
                ('bio', models.TextField(default='Bio', max_length=600)),
                ('phone', models.CharField(default='Phone', max_length=20)),
                ('fname', models.CharField(default='First name', max_length=30)),
                ('lname', models.CharField(default='last name', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]