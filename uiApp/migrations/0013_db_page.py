# Generated by Django 2.2 on 2021-12-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiApp', '0012_db_locator_db_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
