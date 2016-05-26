#Camera receiver on clientside.


import sys
import socket
import pygame
from pygame.locals import *

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()#add proper host
port = 10000
sock_buffer = 16384



pygame.init()
screen = pygame.display.set_mode((640,480))

def display_image():
    sock.connect((host,port))
    data,addr = sock.recvfrom(sock_buffer)
    try:
        while(data):
            screen.blit(data,(0,0))
            sock.settimeout(2)
            data,addr = sock.recvfrom(sock_buffer)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sock.close()
                    sys.exit()
    except:
        sock.close()
        pygame.quit()

    
display_image()
sock.close()
pygame.quit()
sys.exit()
