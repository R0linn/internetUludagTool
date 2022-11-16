import os
import maskpass
from termcolor import colored
print(colored('**********************************************************************************************', 'magenta'))
print(colored(' _____ _   _ _____ ___________ _   _  _____ _____       _   _ _     _   _______  ___  _____', 'green'))
print(colored('|_   _| \ | |_   _|  ___| ___ \ \ | ||  ___|_   _|     | | | | |   | | | |  _  \/ _ \|  __ \ ', 'cyan'))
print(colored('  | | |  \| | | | | |__ | |_/ /  \| || |__   | |       | | | | |   | | | | | | / /_\ \ |  \/', 'green'))
print(colored('  | | | . ` | | | |  __||    /| . ` ||  __|  | |       | | | | |   | | | | | | |  _  | | __  ', 'cyan'))
print(colored(' _| |_| |\  | | | | |___| |\ \| |\  || |___  | |    _  | |_| | |___| |_| | |/ /| | | | |_\ \ ', 'green'))
print(colored(' \___/\_| \_/ \_/ \____/\_| \_\_| \_/\____/  \_/   (_)  \___/\_____/\___/|___/ \_| |_/\____/ ', 'cyan'))
print(colored('                                                                          tool by Altug AKINCI', 'grey',None,['bold']))
print(colored('**********************************************************************************************', 'magenta'))
print(colored('LOGIN ICIN 1, LOGOUT ICIN 0 YAZABILIRSINIZ:', 'green'))
in_or_out = int(input())
print(colored('**********************************************************************************************', 'magenta'))
if in_or_out == 1:
    print(colored('KULLANICI ADI', 'green'), colored('(sonuna @uludag.edu.tr yazmamalısınız!): ', 'red'))
    name = input()
    print(colored('**********************************************************************************************', 'magenta'))
    print(colored('SIFRENIZ: ', 'green'))
    pwd = maskpass.askpass(prompt="",mask="*")
    print(colored('**********************************************************************************************', 'magenta'))
    print(colored('OTURUM SURESI', 'green'), colored('(dakika): ', 'red'))
    time = input()
    print(colored('**********************************************************************************************', 'magenta'))
    cmd = f'curl -X POST -F "login_user={name}" -F "login_pwd={pwd}" -F "login_time={time}" https://internet.uludag.edu.tr/loginLogout.php'

    os.system(cmd)
elif in_or_out == 0:
    print(colored('KULLANICI ADI', 'green'), colored('(sonuna @uludag.edu.tr yazmamalısınız!): ', 'red'))
    name = input()
    print(colored('**********************************************************************************************', 'magenta'))
    print(colored('SIFRENIZ: ', 'green'))
    pwd = maskpass.askpass(prompt="",mask="*")
    print(colored('**********************************************************************************************', 'magenta'))
    cmd = f'curl -X POST -F "logout_user={name}" -F "logout_pwd={pwd}" https://internet.uludag.edu.tr/loginLogout.php'

    os.system(cmd)



