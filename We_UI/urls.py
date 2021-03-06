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
    path('login/', to_login),
    path('user_login/', login),
    path('login_no_user/', login_no_user),
    path('login_pwd_error/', login_pwd_error),
    path('logout/', logout),
    path('accounts/login/', to_login),
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
    path('update_project/', update_project),
    re_path('upload/(?P<case_id>.+)/', upload_script),
    re_path('run_script/(?P<case_id>.+)/', run_script),
    re_path('concurrent_run/(?P<pro_id>.+)/', concurrent_run_script),
    re_path('open_monitor/(?P<pro_id>.+)/', open_monitor),
    re_path('close_monitor/(?P<pro_id>.+)/', close_monitor),
    re_path('look_report/(?P<case_id>.+)/', look_report),
    re_path('download_test_script/(?P<pro_id>.+)/', download_client),
    re_path('look_report_summary/(?P<pro_id>.+)/', look_report_summary),
    re_path('export_report/(?P<pro_id>.+)/', export_report),
    re_path('upload_utils/(?P<pro_id>.+)/', upload_public_utils),
    re_path('upload_page/(?P<pro_id>.+)/', upload_page),
    path('user_list/', user_list),
    path('add_member/', add_user),
    re_path('get_edit_member_msg/(?P<user_id>.+)', get_user_msg),
    path('edit_member/', edit_user),
    re_path('locator_list/(?P<pro_id>.*)', locator_list),
    re_path('add_locator/(?P<pro_id>.+)', add_locator),
    re_path('delete_locator/(?P<loc_id>.+)', delete_locator),
    re_path('get_edit_locator_msg/(?P<loc_id>.+)',get_locator_msg),
    re_path('edit_locator/(?P<loc_id>.+)',edit_locator),
    re_path('open_get_locator/(?P<loc_id>.+)',open_get_locator),
    re_path('open_edits_locator/(?P<loc_id>.+)/',open_edit_locator),

]
