# Generated by Django 4.1.3 on 2023-01-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_rename_staff_pic_staff_staff_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Staff_Pic',
            field=models.FileField(upload_to='Files Upload/team members'),
        ),
    ]