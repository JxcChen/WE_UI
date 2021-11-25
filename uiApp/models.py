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

    def __str__(self):
        return self.name


class DB_cases(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
