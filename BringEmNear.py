import argparse
from tools import snus
from tools import user
from tools import ip

print("""\
 ▄▄▄▄    ██▀███   ██▓ ███▄    █   ▄████    ▓█████  ███▄ ▄███▓    ███▄    █ ▓█████ ▄▄▄       ██▀███  
▓█████▄ ▓██ ▒ ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓█   ▀ ▓██▒▀█▀ ██▒    ██ ▀█   █ ▓█   ▀▒████▄    ▓██ ▒ ██▒
▒██▒ ▄██▓██ ░▄█ ▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒███   ▓██    ▓██░   ▓██  ▀█ ██▒▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒
▒██░█▀  ▒██▀▀█▄  ░██░▓██▒  ▐▌██▒░▓█  ██▓   ▒▓█  ▄ ▒██    ▒██    ▓██▒  ▐▌██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  
░▓█  ▀█▓░██▓ ▒██▒░██░▒██░   ▓██░░▒▓███▀▒   ░▒████▒▒██▒   ░██▒   ▒██░   ▓██░░▒████▒▓█   ▓██▒░██▓ ▒██▒
░▒▓███▀▒░ ▒▓ ░▒▓░░▓  ░ ▒░   ▒ ▒  ░▒   ▒    ░░ ▒░ ░░ ▒░   ░  ░   ░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░
▒░▒   ░   ░▒ ░ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░     ░ ░  ░░  ░      ░   ░ ░░   ░ ▒░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░
 ░    ░   ░░   ░  ▒ ░   ░   ░ ░ ░ ░   ░       ░   ░      ░         ░   ░ ░    ░    ░   ▒     ░░   ░ 
 ░         ░      ░           ░       ░       ░  ░       ░               ░    ░  ░     ░  ░   ░     
      ░                                                                                             
      
Prt's Toolbox for OSINT Investigations
    """)

while True:
    try:
        command = input("> ")

        if command.lower() == "exit":
            break

        if command.lower() == "help":
            print("""\
                user = Search for a username.
                snus = Search Snusbase.
                ip = Find IP location.
                """)

        if command.lower() == "ip":
            ip.ip_search()

        if command.lower() == "user":
            user.search()

        if command.lower() == "snus":
            snus.main()

    except KeyboardInterrupt:
        print("")
        break


