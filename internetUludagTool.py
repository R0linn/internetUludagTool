import os
import maskpass
import subprocess
from termcolor import colored

print(colored(' _____ _   _ _____ ___________ _   _  _____ _____       _   _ _     _   _______  ___  _____', 'green'))
print(colored('|_   _| \ | |_   _|  ___| ___ \ \ | ||  ___|_   _|     | | | | |   | | | |  _  \/ _ \|  __ \ ', 'cyan'))
print(colored('  | | |  \| | | | | |__ | |_/ /  \| || |__   | |       | | | | |   | | | | | | / /_\ \ |  \/', 'green'))
print(colored('  | | | . ` | | | |  __||    /| . ` ||  __|  | |       | | | | |   | | | | | | |  _  | | __  tool', 'cyan'))
print(colored(' _| |_| |\  | | | | |___| |\ \| |\  || |___  | |    _  | |_| | |___| |_| | |/ /| | | | |_\ \ by', 'green'))
print(colored(' \___/\_| \_/ \_/ \____/\_| \_\_| \_/\____/  \_/   (_)  \___/\_____/\___/|___/ \_| |_/\____/ Altug Akinci', 'cyan'))

print(colored('KULLANICI ADI', 'green'), colored('(sonuna @uludag.edu.tr yazmamalısınız!): ', 'red'))
name = input()

print(colored('SIFRENIZ: ', 'green'))
pwd = maskpass.askpass(prompt="",mask="*")

print(colored('OTURUM SURESI', 'green'), colored('(dakika): ', 'red'))
time = input()

cmd = f'curl -X POST -F "login_user={name}" -F "login_pwd={pwd}" -F "login_time={time}" https://internet.uludag.edu.tr/loginLogout.php'

os.system(cmd)
