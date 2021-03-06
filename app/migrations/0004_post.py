# Generated by Django 4.0.5 on 2022-06-20 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_profile_neighborhood_business'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=30)),
                ('post', models.TextField(default='Post', max_length=600)),
                ('image', models.ImageField(upload_to='post_pics')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
