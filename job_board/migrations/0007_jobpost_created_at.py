# Generated by Django 4.1.7 on 2023-04-21 22:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0006_remove_jobpost_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]