# Generated by Django 4.2.5 on 2023-10-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='profile_img'),
        ),
    ]