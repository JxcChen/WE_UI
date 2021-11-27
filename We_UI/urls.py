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
    path('home/',home),
    path('save_end/',save_end),
    re_path('del_end/(?P<del_id>.+)/',del_end),
    re_path('testcases/(?P<pro_id>.+)/',testcases),
    re_path('add_case/(?P<pro_id>.+)/', add_case),
    re_path('edit_case/', edit_case),
    re_path('update_case/(?P<pro_id>.+)',update_case),
    re_path('del_case/', del_case)
]
