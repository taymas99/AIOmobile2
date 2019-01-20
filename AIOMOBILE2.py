import os

def menu():

    print(""" 
████─███─████
█──█──█──█──█
████──█──█──█
█──█──█──█──█
█──█─███─████


█───█─████─████──███─█───███
██─██─█──█─█──██──█──█───█
█─█─█─█──█─████───█──█───███
█───█─█──█─█──██──█──█───█
█───█─████─████──███─███─███
Авторы: Volcano и Pavvlusa
Ютуб канал: https://goo.gl/exVm8X
Вк: https://vk.com/pchirtoca  https://vk.com/taymik
Версия: Бета Версия, номер два
----
Для кектима
----
==========================================
Стань маминым хакером
------------------------------------------
1. Установить DDOS Memcrashed
2. Установить DDOS Version2
3. Install TrackUrl
4. Install DDOS Version3
5. VK TOKEN (может работать не на всех устройствах)
6. Установить Кали НетХантер
7. Установить Метасплоит
8. В разработке
9. В разработке
10. Установить IPGeoLocation
11. В разработке
12. В разработке
13. В разработке
14. В разработке
15. В разработке
16. В разработке
17. В разработке
18. В разработке
19. В разработке
------------------------------------------
99. Exit
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/649/Memcrashed-DDoS-Exploit.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] DDOS Memcrashed установлен")
        print("[+] Напиши python Memcrashed.py для старта")
        print("[+] Инструкция https://lolzteam.net/threads/759010/")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/zanyarjamal/xerxes.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ДДОС Второй версий Установлен, пользуйся")
        print("[+] Для работы напиши ./xerxes.exe fakesite.com ")
        print("[+] Инструкция https://lolzteam.net/threads/755542/")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mauladen/TrackUrl.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] TrackUrl установлен и готов к работе")
        print("[+] Иди в раздел TrackUrl и напиши ./TrackUrl.sh для запуска")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install clang")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/taymas99/goldeneye.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ДДОС Третей версий установлен и работает")
        print("[+] Иди в раздел Goldeneye и напиши python goldeneye.py для старта. Инструкция https://lolzteam.net/threads/761652/")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/prawn-cake/vk-requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] VK TOKEN Установлен и работает")
        print("[+] Иди в раздел VK TOKEN и напиши pip install vk-requests Инструкция https://github.com/prawn-cake/vk-requests")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter Установлен и работает")
        print("[+] Иди в раздел Nethunter-In-Termux folder и напиши ./kalinethunter для старта")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh ")
        print("====================================")
        print("[+] МетаСплоит готов работать")
        print("[+] Напиши msfconsole ")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n):  ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clonefffffhttps://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK installed successfully :)")
        print("[+] Go to RED_HAWK folder and type 'php rhawk.php' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n):  ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone htfffftps://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman installed successfully :)")
        print("[+] Go to weeman folder and type 'python2 weeman.py' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation installed successfully :)")
        print("[+] Go to IPGeoLocation folder and type 'python ipgeolocation.py' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n):  ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone htffftps://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp installed successfully :)")
        print("[+] Go to cupp folder and type 'python cupp3.py' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://ffgithub.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack installed successfully :)")
        print("[+] Go to instahack folder and type 'python hackinsta.py' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://gffithub.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper installed successfully :)")
        print("[+] Go to TwitterSniper folder and type 'python TwitterSniper.py' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://gifffthub.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu installed successfully :)")
        print("[+] Go to termux-ubuntu folder and type './start.sh' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/ffffiles/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora installed successfully :)")
        print("[+] Type 'sh termux-fedora.sh f26_arm64' or 'sh termux-fedora.sh f26_arm' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://githfffub.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL installed successfully :)")
        print("[+] Go to viSQL folder and type 'python2 viSQL.py --help' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://githfffub.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://githffffub.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://gfffithub.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit installed successfully :)")
            print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
            print("====================================")
            rmenu = input("[?] Обратно в меню? Y-да, n- нет (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "99":
        print("Пока, не забудь оставить отзыв!")
        break
