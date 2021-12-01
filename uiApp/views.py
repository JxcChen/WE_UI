import json
import shutil
import subprocess

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
    new_client = os.path.join(base_path, r"my_client/client_" + str(end.id))
    shutil.copytree(demo_path, new_client)
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
    return HttpResponse('')


# 上传脚本
def upload_script(request, case_id):
    # 拿到端id
    pro_id = DB_cases.objects.filter(id=case_id)[0].pro_id
    # 获取到上传的脚本
    my_file = request.FILES.get("script_file", None)
    # 如果文件为空则直接返回
    if not my_file:
        return HttpResponseRedirect('/testcases/' + pro_id + '/')
    # 获取文件名称
    file_name = str(my_file)
    # 打开本地文件
    with open("uiApp/my_client/client_%s/case/%s" % (pro_id, file_name), 'wb') as file:
        for content in my_file.chunks():
            file.write(content)
    # 将文件名称存到数据库
    DB_cases.objects.filter(id=case_id).update(script=file_name)
    # 返回
    return HttpResponseRedirect('/testcases/%s/' % pro_id)


def del_case(request):
    case_id = request.GET['case_id']
    pro_id = request.GET['pro_id']
    DB_cases.objects.filter(id=case_id).delete()

    return HttpResponseRedirect('/testcases/' + pro_id + '/')


# 运行脚本
def run_script(request,case_id):
    print("+++++")
    case = DB_cases.objects.filter(id=case_id)[0]
    pro_id = case.pro_id
    script_name = case.script
    # 判断是否未上传脚本文件
    if script_name in ['',' ',None,'None']:
        return HttpResponse('Error')
    # 执行py文件
    subprocess.call('python uiApp/my_client/client_%s/case/%s' % (pro_id, script_name),shell=True)
    return HttpResponse('Success')


# 获取项目信息
def get_project_msg(request, pro_id):
    pro_msg = list(DB_end.objects.filter(id=pro_id).values())[0]
    return HttpResponse(json.dumps(pro_msg), content_type="application/json")


# 编辑项目
def update_project(request):
    DB_end.objects.filter(id=request.GET['pro_id']).update(name=request.GET['pro_name'], host=request.GET['pro_host'],
                                                           check_time=request.GET['check_time'],
                                                           phone=request.GET['phone'], email=request.GET['email'],
                                                           dingtalk=request.GET['dingtalk'],
                                                           max_threads=request.GET['max_threads'], )
    return HttpResponseRedirect("/home/")
