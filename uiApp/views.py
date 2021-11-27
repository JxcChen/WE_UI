import json
import shutil

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
    end = DB_end.objects.create(name=pro_name, host=pro_host, email=pro_email)
    base_path = os.path.dirname(os.path.abspath(__file__))
    demo_path = os.path.join(base_path, r"my_client/demo_client")
    new_client = os.path.join(base_path, r"my_client/client_"+str(end.id))
    shutil.copytree(demo_path,new_client)
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

    DB_cases.objects.create(pro_id=pro_id, name=request.GET['case_name'], retry_count=request.GET['retry_count'],
                            is_monitor=is_monitor, is_threads=is_threads, case_type=request.GET['case_type'])

    return HttpResponseRedirect('/testcases/' + pro_id + '/')


def edit_case(request):
    case_id = request.GET['id']
    case = list(DB_cases.objects.filter(id=case_id).values())[0]
    return HttpResponse(json.dumps(case), content_type="application/json")


def update_case(request, pro_id):
    is_monitor = False
    if request.GET['is_monitor'] == "True":
        is_monitor = True

    is_threads = False
    if request.GET['is_monitor'] == "True":
        is_monitor = True
    case_id = request.GET['case_id']

    DB_cases.objects.filter(id=case_id).update(name=request.GET['case_name'], retry_count=request.GET['retry_count'],
                                               is_monitor=is_monitor, is_threads=is_threads,
                                               case_type=request.GET['case_type'])
    return HttpResponseRedirect('/testcases/'+ pro_id + '/')


def del_case(request):
    case_id = request.GET['case_id']
    pro_id = request.GET['pro_id']
    DB_cases.objects.filter(id=case_id).delete()

    return HttpResponseRedirect('/testcases/'+ pro_id + '/')