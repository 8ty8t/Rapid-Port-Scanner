import pyfiglet 
from datetime import datetime
import time
import socket
import threading
import requests
from colorama import Fore, Back, Style, init

init()

my_ip = requests.get("http://ip.42.pl/raw").text
print(Fore.RED + "DETAILS:")
print(Fore.YELLOW + "Hostname:",socket.gethostname())
print(Fore.YELLOW + "Local", socket.gethostbyname(socket.gethostname()))
print(Fore.YELLOW+ "Public :", my_ip)
ascii_banner = pyfiglet.figlet_format("portsc", font = "slant") 
print(Fore.CYAN + ascii_banner)

target = input("IP TO SCAN : ")
timeout = input("SET TIMEOUT (S) : ")
start_port = int(input("STARTING PORT : "))
end_port = int(input("ENDING PORT : "))
#ip = socket.gethostname()
portoo = 1
openports = 0
start = time.time()
def portscan(port1, port):
    global portoo
    global openports
    global timeout
    for i in range(port1, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(float(timeout))

        try:
            con = s.connect((target,port1))

            print(Fore.GREEN + '[+] Port :',port1,"is open" + Fore.RESET)
            openports = openports + 1

            con.close()
        except:
            print(Fore.RED + "[-] Scanning Port", port1, end="\r" + Fore.RESET)
        port1 = port1 + 1
    end = time.time()
    howlong = end - start
    print(Fore.CYAN + "--------------------------")
    if openports == 0:
        print(Fore.RED + "[-] Scan Completed,", openports, "Ports Open" + Fore.RESET)
    else:
        print(Fore.MAGENTA + "[+] Scan Completed,", openports, "Ports Open" + Fore.RESET)
    print("That Took", howlong, "Seconds!")
    print(Fore.CYAN)
    whatdo = input("ENTER To Exit")
    if whatdo == "q":
        exit()
    else:
        exit()

t1 = threading.Thread(target=portscan, args=(start_port,end_port,))
t1.start()
