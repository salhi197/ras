import socket
import serial
from time import sleep
#   apt-get install mpg321

ser = serial.Serial(
                        port='/dev/serial0',
                        baudrate = 115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1
                )

print("yooooooooooooo")
HOST = '192.168.8.200'                 # Symbolic name meaning all available in$
PORT = 50007              # Arbitrary non-privileged port
while True:
 sleep(.300)
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            p=data.decode('utf-8')
            # get all audios 
            audios = os.listdir('./audios')
            audio_file_name = audios[p]
            audio_file = "/audios/"+audio_file_name
            cmd = 'mpg321 '+audio_file+' &'
            os.system(cmd)
            # entrer le code dans l espace en haut
            #print(data)
            #print(type(data))
            #print(p)
            #print(type(p))
            #k = bytes(p, 'utf-8')
            b = bytes(p, 'UTF-8')
            x=bytearray(b)
             #ser.write(x)
            received_data = ser.write(x)
 #           n= ser.write("700" + str(x))
             #read serial port
            print(p)
            print(b)
            print(x)
            sleep(3)
            ser.flush()
            if not data: break
