# python 3.7.9
import string
import random
import sys
import os
import subprocess
import shutil
import time

working_dir = os.path.dirname(os.path.realpath(__file__))

def main():
    print('깃헙 기여 작업 스케줄러 등록\n')
    if not sys.platform.startswith('win32'):
        print('윈도우 운영체제에서만 자동 등록이 가능합니다.')
        return
    delay = '1M'
    indly = input('로그인 후 실행 딜레이 입력 (1M, 5M, 10M, 1H, 2H, def: 1M): ')
    if len(indly.replace('\n', '').replace(' ', '')) >= 1:
        delay = indly.upper()
    generator_path = join_working_dir('garbage-generator.py')
    hide_generator_path = generator_path + 'w'
    shutil.copy(generator_path, hide_generator_path)

    command = hide_generator_path
    wkdir = working_dir
    template = open(join_working_dir('garbage-generator-template.xml'), mode='r', encoding='utf-8').read()

    st_id = random_string(6)
    task_scheduler_config_path = join_working_dir('garbage-generator-config_' + st_id + '.xml')
    task_scheduler_config = open(task_scheduler_config_path, mode='wt', encoding='utf-8')
    task_scheduler_config.write(template.replace('{/command}', command).replace('{/wkdir}', wkdir).replace('{/delay}', delay))
    task_scheduler_config.flush()
    task_scheduler_config.close()

    exit_code = subprocess.call(['powershell', 'Start-Process', 'schtasks', '-ArgumentList', '"/create",', 
        '"/xml",', '"' + task_scheduler_config_path + '",', '"/tn",', '"garbage-generator_' + st_id + '"', '-Wait', '-Verb', 'runAs'])
    if exit_code == 0:
        print('등록 성공.')
    else: print('등록 실패.')
    if os.path.isfile(task_scheduler_config_path):
        os.remove(task_scheduler_config_path)

# os.path.join
def join_working_dir(file):
    return os.path.join(working_dir, file)
    
# random string a-z A-Z 0-9
def random_string(size=48, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

main()
time.sleep(1)
