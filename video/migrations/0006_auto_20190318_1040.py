# Generated by Django 2.2b1 on 2019-03-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20190318_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='folder_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='folder',
            name='folder_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
