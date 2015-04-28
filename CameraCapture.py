#create listening connection
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 10000
sock.bind((host,port))

sock_buffer = 16384

pygame.init()
pygame.camera.init()
camList = pygame.camera.list_cameras()
cam0 = pygame.camera.Camera(camList[0])
cam0.start()

sock.listen(5)
#continuously update cImage and send to a socket.
while True:
        conn,addr = sock.accept()
        print "connection from ", addr
        print "sending test video"
        
        cImage = cam0.get_image()
        cImage = pygame.transform.scale(cImage,(640,480))
        data = pygame.image.tostring(cImage,"RGB")

        while(data):
                conn.sendto(data,addr)
                cImage = cam0.get_image()
                cImage = pygame.transform.scale(cImage,(640,480))
                data = pygame.image.tostring(cImage,"RGB")
        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        cam0.stop()
                        pygame.quit()
                        sys.exit()
