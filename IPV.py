#!/usr/bin/python3

import socket
import requests
import stun

#Interractive panel with user
print("Enter params:\n "
      "1. View Web-IP of local machine.\n "
      "2. View server status. \n "
      "3. View any web server IP.\n "
      "4. Exit. \n "
      "Press 1-4 for choose\n")

#Moving the input into a universal variable
inp = input()

#Get local machine web ip with stun library
if inp == '1':
    ip = stun.get_ip_info()
    print(f'You IP is: {ip}')

#Get status code of any server(1xx,2xx,3xx,4xx,5xx) with requests library
elif inp == '2':
    response = input('Input url( ex. https://www.google.ru/ ):\n')
    print('Server status is:\n',requests.get(response))

#Get any web-site ip-address with socket library
elif inp == '3':
    host_name = input('Enter the web-site address(ex. www.google.ru ):\n')
    print(f'The {host_name} IP address is: {socket.gethostbyname(host_name)}')

#Exit option
elif inp == '4':
    print('Exit')



"""---Development by Puma---"""
"""GPL3"""
