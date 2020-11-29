#!/usr/bin/python3
try:
  import nmap, sys
except ImportError:
  print("[+] Error in lib")

def banner():
  print('''\033[31m
 ██████╗ ██████╗ ██████╗  █████╗ ██╗
\033[32m██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██║
\033[35m██║   ██║██████╔╝██████╔╝███████║██║
\033[32m██║   ██║██╔═══╝ ██╔═══╝ ██╔══██║██║
\033[36m╚██████╔╝██║     ██║     ██║  ██║██║
\033[31m ╚═════╝ ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝
\033[0;0m
  ''')
  print("\033[33m-\033[0;0m" * 60)
  print('\033[32m[*]\033[0;0m Scanning...')
  print("\033[31m-\033[0;0m" * 60)
def scan():
  #variaveis...
  host = sys.argv[1]
  scanp = nmap.PortScanner()
  scanp.scan(host , '1-65535')  
  for host in scanp.all_hosts():
    print("\033[31m-\033[0;0m" * 60)
    print(f'\033[32m[*]\033[0;0m Host :: {host} :: {scanp[host].hostname()}' )
    print("\033[33m-\033[0;0m" * 60)
    print(f'\033[32m[*]\033[0;0m State :: {scanp[host].state()}' )    
    print("\033[31m-\033[0;0m" * 60)
    
    for proto in scanp[host].all_protocols():
      print(f'\033[32m[*]\033[0;0m Protocol :: {proto}')
      print("\033[33m-\033[0;0m" * 60)
      
      phost = scanp[host][proto].keys()
      
      for port in phost:
        print(f'\033[32m[*]\033[0;0m Port :: {port} :: {scanp[host][proto][port]["state"]}')

try:  
  if len(sys.argv) >= 2:
    banner()
    scan()
  else:
    print('\033[41m[!]\033[0;0m Usage : ./scanp2 <target>')
except KeyboardInterrupt:
  print('\033[41m[!]\033[0;0m Stop')
