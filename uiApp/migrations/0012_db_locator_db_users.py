# Generated by Django 2.2 on 2021-12-20 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiApp', '0011_db_end_monitor_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_locator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('page', models.CharField(blank=True, max_length=50, null=True)),
                ('tmp_method', models.CharField(blank=True, max_length=30, null=True)),
                ('tmp_value', models.CharField(blank=True, max_length=200, null=True)),
                ('tag', models.CharField(blank=True, max_length=300, null=True)),
                ('index', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DB_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('has_project', models.CharField(max_length=50)),
            ],
        ),
    ]
