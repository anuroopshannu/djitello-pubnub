import threading
import socket
import sys
import time
import pubnub

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub          import PubNub, SubscribeListener


pnconfig = PNConfiguration()
pnconfig.publish_key = "*************************"
pnconfig.subscribe_key = "************************"

pubnub = PubNub(pnconfig)

host = ''
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)


class MyListener(SubscribeListener):
    def message( self, pubnub, data ):
        print( "Saving to Database: ", data.message )
        rmsg = data.message
        if(rmsg=="fly droopie fly"):
            msg="takeoff"
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        elif(rmsg=="where is my heart"):
            msg="left"
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        elif(rmsg=="palti maro"):
            msg="flip r"
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        elif(rmsg=="land"):
            msg="land"
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        elif(rmsg=="right"):
            msg="right"
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        elif(rmsg=="yaw"):
            msg="cw"
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        elif(rmsg=="back"):
            msg="back"
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        elif(rmsg=="fwd"):
            msg="forward"
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)





def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nFoGR Tello Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


msg="command"
msg = msg.encode(encoding="utf-8")
sent = sock.sendto(msg, tello_address)
print("listening...")

pubnub.add_listener(MyListener())
pubnub.subscribe().channels("fogr").execute()
