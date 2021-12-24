# coding: utf-8

import os
import platform
import subprocess
import sys
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import requests

path = os.path.dirname(os.path.dirname(__file__))
print(path)
sys.path.append(path)

# 设置环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'We_UI.settings'
import django

# 启动django
django.setup()

from uiApp.models import *
from uiApp.views import *


def send_report_email():
    """
    通过邮件方式发送测试报告
    """
    # 先获取报告内容
    response = look_report_summary({}, pro_id)
    mail_content = response.content.decode()
    # 声明邮件信息
    mail_send = "360088940@qq.com"
    mail_receive = "838386443@qq.com"
    mail_host = "smtp.qq.com"  # 声明发送服务器名称
    mail_secret = "wjotabdwqkilcaei"
    # 声明邮件格式
    text = MIMEText(mail_content, "html", 'utf-8')
    msg = MIMEMultipart('related')
    msg['From'] = mail_send
    msg['To'] = mail_receive
    msg['Subject'] = '%s项目 UI自动化测试报告' % project.name
    msg.attach(text)  # 设置邮件装载
    try:
        # 获取邮件服务
        server = smtplib.SMTP()
        # 设置服务名称、发件人和收件人信息
        server.connect(mail_host)
        server.login(mail_send, mail_secret)
        server.sendmail(mail_send, mail_receive, msg.as_string())
        print("邮件发送成功")
        server.close()
    except Exception as e:
        print("邮件发送失败")
        raise e


def send_report_wechat():
    """
    以企微方式推送报告消息
    """
    # 先获取报告内容

    response = look_report_summary({}, pro_id)
    report_content = response.content.decode()
    wechat_url = project.dingtalk
    header = {'Content-Type': 'application/json'}
    data = {"msgtype": "text",
            "text": {
                "content": report_content
            }
            }
    response = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6abe65f6-be65-43cd-b252-6ca5948abc47",
        data=json.dumps(data), headers=header)



def monitor():
    # 启动一个无限循环  一直进行监控
    while True:
        # 获取到对应项目需要进行监控的用例
        cases = DB_cases.objects.filter(pro_id=pro_id, is_monitor=True)
        for case in cases:
            if case not in ['', None, ' ', 'None']:
                if '.py' in case.script:
                    if operation == 'Windows':
                        subprocess.call('python my_client/client_%s/case/%s %s %s %s' % (
                            case.pro_id, case.script, project.monitor_host, case.script, case.name), shell=True)
                    else:
                        subprocess.call('python3 my_client/client_%s/case/%s %s %s %s' % (
                            case.pro_id, case.script, project.monitor_host, case.script, case.name), shell=True)
                elif '.xls' in case.script:
                    if operation == "Windows":
                        subprocess.call('python my_client/client_%s/public/xls_to_script.py %s %s %s' % (
                            case.pro_id, project.monitor_host, case.script, case.name), shell=True)
                    else:
                        subprocess.call('python3 my_client/client_%s/public/xls_to_script.py %s %s %s' % (
                            case.pro_id, project.monitor_host, case.script, case.name), shell=True)
        print('本轮测试执行完毕')
        send_report_wechat()
        time.sleep(project.check_time)


if __name__ == '__main__':
    operation = platform.system()
    # 获取到系统传入的第一个参数
    pro_id = sys.argv[1]
    project = DB_end.objects.filter(id=pro_id)[0]
    monitor()
