# Generated by Django 2.2 on 2021-11-25 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiApp', '0002_db_end'),
    ]

    operations = [
        migrations.RenameField(
            model_name='db_end',
            old_name='end_url',
            new_name='dingtalk',
        ),
        migrations.AddField(
            model_name='db_end',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='db_end',
            name='host',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='db_end',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]