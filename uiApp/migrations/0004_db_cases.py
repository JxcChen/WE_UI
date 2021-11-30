# Generated by Django 2.2 on 2021-11-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiApp', '0003_auto_20211125_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('case_type', models.IntegerField(blank=True, default=0, null=True)),
                ('is_monitor', models.BooleanField(blank=True, default=True, null=True)),
                ('script', models.CharField(blank=True, max_length=200, null=True)),
                ('is_threads', models.BooleanField(blank=True, default=True, null=True)),
                ('pro_id', models.CharField(max_length=20)),
            ],
        ),
    ]