# python 3.7.9
import subprocess
import time

def main():
    print('목록 불러오는중...')
    output = subprocess.check_output(['schtasks']).decode('ansi')

    print('항목 찾는중...')
    tasks = find_tasks(output)
        
    tasks_len = len(tasks)
    if tasks_len <= 0:
        print('항목 없음.')
        return
        
    print('항목 제거중...')

    args = list([ 'powershell', 'Start-Process', 'cmd', '-ArgumentList', "'/c'," ])
    i = 0
    for item in tasks:
        add_task_delete_script(args, item, i >= tasks_len - 1)
        i += 1
    args.append('-Wait')
    args.append('-Verb')
    args.append('runAs')
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    exit_code = subprocess.call(args, startupinfo=si)
    if exit_code == 0:
        print('제거 성공.')
    else: print('제거 실패.')

def find_tasks(output: str):
    output_len = len(output)
    findstr = 'garbage-generator_'
    findstr_len = len(findstr)
    tasks = [ ]
    i = 0
    while True:
        i = output.find(findstr, i + 1)
        if i == -1: break
        s = findstr
        l = i + findstr_len
        while output[l] and output[l] != ' ':
            s += output[l]
            l += 1
            if output_len <= l: break
        tasks.append(s)
        print(s)
    return tasks

def add_task_delete_script(args: list, task_name: str, is_end: bool):
    args.append("'schtasks',")
    args.append("'/delete',")
    args.append("'/tn',")
    args.append("'\"" + task_name + "\"',")
    if not is_end: 
        args.append("'/f',")
        args.append("'&&',")
    else: args.append("'/f'")


main()
time.sleep(1)
