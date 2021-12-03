import os
import subprocess
import sys
import time

path = os.path.dirname(os.path.dirname(__file__))
print(path)
sys.path.append(path)

import django
# 设置环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'We_UI.settings'
# 启动django
django.setup()
from uiApp.models import *


def monitor():
    # 启动一个无限循环  一直进行监控
    while True:
        project = DB_end.objects.filter(id=pro_id)[0]
        # 获取到对应项目需要进行监控的用例
        cases = DB_cases.objects.filter(pro_id=pro_id, is_monitor=True)
        for case in cases:
            if case not in ['', None, ' ', 'None']:
                print(case.script)
                subprocess.call('python my_client/client_%s/case/%s' % (pro_id, case.script), shell=True)
        print('本轮测试执行完毕')
        time.sleep(project.check_time)


if __name__ == '__main__':
    # 获取到系统传入的第一个参数
    pro_id = sys.argv[1]
    monitor()
