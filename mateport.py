import ipaddress,socket,threading,click
from colorama import Fore, Back, Style,init,deinit
import _thread as thread
""" Importing Liberals that in use threading and etc... """

class Process_port(threading.Thread):
    """ This is object is scanning each IP for open port """
    
    def __init__(self,ip,port,thread_name):
        super(Process_port,self).__init__()
        self.ip = ip # makeing ip read to use 
        self.port = port # makeing port read to use  
        self.thread_name = thread_name #makeing thread_name read to use 
        
    def run(self):
        """ This object gon be called automatic every time that main object get called """

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket 
        ip = ipaddress.IPv4Address(self.ip) # converting ip from raw date to IP v4
        result = sock.connect_ex((str(ip),self.port)) # trying to connect to the sever and cheak if ip is open
        if result == 0: # if we found port result go return value of 0
            print ("[open] IP :",str(ip),"PORT:",str(self.port),"thread :",self.thread_name)
            sock.close() #closing sock 
            with open("goods.txt","a") as file : file.write(str(ip)+":3389\n")
        else: #if we didnt found port result go return value of 1
            print ("[Close] IP :",str(ip),"PORT:",str(self.port),"thread :",self.thread_name)
            sock.close() #closing sock 


thread_list = [] #Makeing list for storing Thread in it 

def main(file,port=3389,workers=4001):
    """this def gon read the file and call the workers"""
    with open(file,"r") as file: #opeing the file 

        file = file.readlines() # reading all lines in file 

        for ranges in file: #reading file line by line 

            if ranges.strip("\n"): #removing empty line form file

                """Converting lines to ips and ips to range """

                IpStartBase = ranges.strip().split("-")[0]
                IpEndBase = ranges.strip().split("-")[1]

                StartIp = ipaddress.IPv4Address(IpStartBase)
                Endip = ipaddress.IPv4Address(IpEndBase)


                for ip in range(int(StartIp),int(Endip)): #Looping from ranges of ip 
                    try:
                        """"Checking if we have more then SetLimet threads and if not start the new thread"""
                        while True:
                            if len(threading.enumerate()) < workers: 
                                thread_ = Process_port(ip,port,thread._count())
                                thread_.daemon = True
                                thread_.start()
                                thread_list.append(thread_)
                                break
                    except KeyboardInterrupt: #if users Interrupt the cod do this 
                        init() #we gon call init object form Colorama so we can use windows don't filter ANSI 
                        print(Fore.RED+"Look Like We are done Hare!")
                        quit() #quit 
                        break # break the loop 
               
                        
                
    for t in thread_list:
        """ Joining threads together """
        t.join()

if __name__ == "__main__":
    click.clear()
    try:
        print(Fore.MAGENTA+"""\n\n\n
   /$$      /$$             /$$               /$$$$$$$                       /$$    
  | $$$    /$$$            | $$              | $$__  $$                     | $$    
  | $$$$  /$$$$  /$$$$$$  /$$$$$$    /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$  /$$$$$$  
  | $$ $$/$$ $$ |____  $$|_  $$_/   /$$__  $$| $$$$$$$//$$__  $$ /$$__  $$|_  $$_/  
  | $$  $$$| $$  /$$$$$$$  | $$    | $$$$$$$$| $$____/| $$  \ $$| $$  \__/  | $$    
  | $$\  $ | $$ /$$__  $$  | $$ /$$| $$_____/| $$     | $$  | $$| $$        | $$ /$$
  | $$ \/  | $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$     |  $$$$$$/| $$        |  $$$$/
  |__/     |__/ \_______/   \___/   \_______/|__/      \______/ |__/         \___/  
  """+Back.YELLOW+"""\n\t\t4D 61 74 65 50 6F 72 74 By:SH4H1N github.com/Sh4h1n"""+
     Style.RESET_ALL,end="\n\n")
        init(autoreset=True)#we gon call init object form Colorama so windows don't filter ANSI  

        """Geting that form users"""
        print(Fore.YELLOW+"\t[~]"+Fore.GREEN+"Plase Enter IpRange File Patch",end='')
        file = click.prompt(">> ",type=str)
        print(Fore.YELLOW+"\t[~]"+Fore.GREEN+"Plase Enter Port Nummber exp{3389} ",end='')
        port = click.prompt(">> ",default=3389,type=int)
        print(Fore.YELLOW+"\t[~]"+Fore.GREEN+"Plase Enter Thread Nummber exp{4555}",end='')
        workers = click.prompt(">> ",default=4501,type=int)
       
        deinit()#we gon call deinit object form Colorama so Command line go back to normall  

        main(file,port,workers) #calling main def 

    except :
        """ if anything bad happend just exit """
        init()  #we gon call init object form Colorama so we can use windows don't filter ANSI 
        print(Fore.RED+"Error, Some Thing Didnt GO as Plasn!!")
        quit() #quit 
