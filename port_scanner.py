# from socket import*
# def conScanner (tgtHost , tgtPort):
#     try:
#         conn = socket(AF_INET,SOCK_STREAM)
#         conn.connect((tgtHost,tgtPort))
#         print("[+]%d/tcp open"% tgtPort)
#         conn.close()
    
#     except:
#         print ("[-]%d/tcp closed"% tgtPort)

# def prtScan(tgtHost , tgtPorts):
#     try:
#         tgtIP=gethostbyname(tgtHost)
#     except:
#        print ("[-] connection resolved %d" % tgtHost )
       
#     try:
#          tgtname= gethostbyaddr(tgtIP)
#          print("\n[+] scan result of : %s  " %tgtname[0])
#     except:
#         print("\n[+] scan result of : %s  " %tgtIP)
#     setdefaulttimeout(1)
#     for tgtPort in tgtPorts:
#         print('scanning port %d' % tgtPort)
#         conScanner(tgtHost , int(tgtPort))

    




from socket import*
def port_scan(host,port):
        try:
            conn=socket(AF_INET, SOCK_STREAM)
            conn.settimeout(1)
            result=conn.connect((host,port))
            ip=gethostbyname(host)
            hostname=gethostbyaddr(host)
            print(f"ip of {host} is {ip} \n and \n hostname of {ip}is{hostname}") 
            if result==0:
                print(f"[+]{port}/tcp open")
            else:
                print(f"[-]{port}/tcp closed");

            conn.close();
        except:
            print(conn.error() , "ERROR");
            
def prtscans(host , ports):
    try:
        tgtIP=gethostbyname(host)
        print(f"\n the ip of {host} is {tgtIP}")
    except:
       print ("[-] connection resolved %d" % host )
       
    try:
         tgtname= gethostbyaddr(tgtIP)
         print("\n[+] scan result of : %s  " %tgtname[0])
    except:
        print("\n[+] scan result of : %s  " %tgtIP)
    setdefaulttimeout(1)
    for port in ports:
        print('scanning port %d' % port)
       
        port_scan(host,int(port));
# code ends here

port_scan('google.com',80)
prtscans('yahoo.com',(80,443))
   



