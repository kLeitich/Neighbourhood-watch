# Generated by Django 4.0.5 on 2022-06-21 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_post_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.neighborhood'),
        ),
    ]
