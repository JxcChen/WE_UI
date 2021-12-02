"""We_UI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from uiApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('save_end/', save_end),
    re_path('del_end/(?P<del_id>.+)/', del_end),
    re_path('testcases/(?P<pro_id>.+)/', testcases),
    re_path('add_case/(?P<pro_id>.+)/', add_case),
    path('edit_case/', edit_case),
    re_path('update_case/(?P<pro_id>.+)/', update_case),
    path('del_case/', del_case),  # 没有待正则的不需要使用re_path
    re_path('get_project_msg/(?P<pro_id>.+)/', get_project_msg),
    path('update_project/',update_project),
    re_path('upload/(?P<case_id>.+)/', upload_script),
    re_path('run_script/(?P<case_id>.+)/',run_script),
    re_path('concurrent_run/(?P<pro_id>.+)/',concurrent_run_script)
]
