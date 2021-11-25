from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from uiApp.models import *

# Create your views here.

"""
视图逻辑层
"""


# 需要先修改setting.py 才有home.html联想
def home(request):
    res = {'end': DB_end.objects.all(), 'href': DB_href.objects.all()}
    return render(request, 'home.html', res)


def save_end(request):
    pro_name = request.GET['name']
    pro_host = request.GET['host']
    pro_email = request.GET['email']
    DB_end.objects.create(name=pro_name, host=pro_host, email=pro_email)
    return HttpResponse("")


def del_end(request, del_id):
    DB_end.objects.filter(id=del_id).delete()
    return HttpResponseRedirect("/home/")


def testcases(request, pro_id):
    cases = DB_cases.objects.filter(pro_id=pro_id)
    project = list(DB_end.objects.filter(id=pro_id))[0]
    param = {"cases": cases, "project": project}
    return render(request, 'case.html', param)


def add_case(request, pro_id):
    is_monitor = False
    if request.GET['is_monitor'] == "True":
        is_monitor = True

    is_threads = False
    if request.GET['is_monitor'] == "True":
        is_monitor = True
    print("===========" + pro_id)
    DB_cases.objects.create(pro_id=pro_id, name=request.GET['case_name'], retry_count=request.GET['retry_count'],
                            is_monitor=is_monitor, is_threads=is_threads, case_type=request.GET['case_type'])
    cases = DB_cases.objects.filter(pro_id=pro_id)
    project = list(DB_end.objects.filter(id=pro_id))[0]
    param = {"cases": cases, "project": project}
    return render(request, 'case.html', param)
