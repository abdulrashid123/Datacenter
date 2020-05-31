# Generated by Django 2.2b1 on 2019-03-12 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_title', models.CharField(max_length=250)),
                ('video_file', models.FileField(default='', upload_to='')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Folder')),
            ],
        ),
    ]
