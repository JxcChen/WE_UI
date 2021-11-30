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
    check_time = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    dingtalk = models.CharField(max_length=200, null=True, blank=True)
    user = models.CharField(max_length=20, null=True, blank=True)
    max_threads = models.IntegerField(default=5)

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
