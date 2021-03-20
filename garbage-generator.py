# python 3.7.9
import string
import random
import subprocess

def main():
    i = 0
    rgf = open('./garbage', mode='wt', encoding='utf-8')
    print('\n')
    while i < 24:
        rand = random_string()
        rgf.write(rand + '\n')
        print(rand)
        i += 1
    rgf.flush()
    rgf.close()
    # git upload
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.Popen(['git', 'add', '--all'], startupinfo=si).wait()
    subprocess.Popen(['git', 'commit', '-m', 'asd'], startupinfo=si).wait()
    subprocess.Popen(['git', 'push'], startupinfo=si).wait()
    print('\ndone.')

# random string a-z A-Z 0-9
def random_string(size=48, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

main()