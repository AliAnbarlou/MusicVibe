# Generated by Django 5.0.2 on 2024-03-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0004_alter_music_class_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_class',
            name='audio_file',
            field=models.FileField(upload_to='media/audio/'),
        ),
        migrations.AlterField(
            model_name='music_class',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
