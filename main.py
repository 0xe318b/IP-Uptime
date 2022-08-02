import socket
from icmplib import ping
import time
import threading
from colorama import Fore as c


def x():
    
    ###########################
    IP = 'change me'
    # change IP to an ip you want to monitor then run it
    ###########################
    
    try:
        x = str(ping(IP)).replace(" ","")
        lines = x.splitlines()
        for i in lines:
            if i.find("Packetloss") == 0:
                loss = i.replace("Packetloss:","").replace("%","")
                if float(loss) == 100:
                    print(c.RED+"IP IS DOWN!",str(float(loss))+"%")
                elif float(loss) >= 80 and float(loss) <= 65:
                    print(c.LIGHTRED_EX+"IP IS DANGEROUSLY CLOSE TO BEING DOWN!",str(float(loss))+"%")
                elif float(loss) <= 64 and float(loss) >= 35:
                    print(c.YELLOW+"IP IS DECENT!",str(float(loss))+"%")
                else:
                    print(c.GREEN+"IP IS UP |",str(float(loss))+"%")
    except:
        pass
threading.Thread(target=x).start()
for i in range(50000):
    time.sleep(0.5)
    threading.Thread(target=x).start()
