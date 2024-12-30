# Generated by Django 5.1.3 on 2024-12-04 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='category',
            field=models.CharField(choices=[('Timely Project Completion', 'Timely Project Completion'), ('Management Ratings', 'Management Ratings'), ('Daily Projects Reports', 'Daily Projects Reports'), ('Design Proficiency', 'Design Proficiency'), ('Inspection', 'Inspection'), ('Overall Client Rating', 'Overall Client Rating')], max_length=100),
        ),
    ]
