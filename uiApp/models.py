import os

from django.db import models


# Create your models here.


class DB_href(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class DB_end(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    host = models.CharField(max_length=200, null=True, blank=True)
    check_time = models.IntegerField(default=60)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    dingtalk = models.CharField(max_length=200, null=True, blank=True)
    user = models.CharField(max_length=20, null=True, blank=True)
    max_threads = models.IntegerField(default=5)
    monitor_host = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class DB_cases(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    case_type = models.IntegerField(default=0, null=True, blank=True)
    is_monitor = models.BooleanField(default=True, null=True, blank=True)
    script = models.CharField(max_length=200, null=True, blank=True)
    is_threads = models.BooleanField(default=True, null=True, blank=True)
    pro_id = models.CharField(max_length=20, null=False, blank=False)
    retry_count = models.IntegerField(default=2)

    def __str__(self):
        return self.name


class DB_users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    has_project = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class DB_locator(models.Model):
    pro_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    page = models.CharField(max_length=50, null=True, blank=True)
    tmp_method = models.CharField(max_length=30, null=True, blank=True)
    tmp_value = models.CharField(max_length=200, null=True, blank=True)
    tag = models.CharField(max_length=300, null=True, blank=True)
    index = models.IntegerField(default=0)  # 下标

    def __str__(self):
        return self.name


class DB_page(models.Model):
    pro_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
