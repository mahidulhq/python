import socket

def get():
    hostname = input("Website URL AKA Hostname:")
    try:
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')

get()