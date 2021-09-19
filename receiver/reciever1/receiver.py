from scapy.all import *
from scapy.contrib import coap
import time
import convert

lastpkt=0
firstpkt=True
msg=[]

short=0.2
med=0.4
long=0.6

def recv(packet):
    global firstpkt
    global lastpkt
    global msg
    if packet.haslayer(coap.CoAP):
        if packet[IP].dst == "10.10.0.3" and packet[coap.CoAP].type == 3:
            if firstpkt:
                firstpkt = False
                lastpkt = time.time()
            else:
                now=time.time()
                if now-lastpkt < med:
                    msg.append(0)
                elif now-lastpkt < long:
                    msg.append(1)
                else:
                    msg.append(2)
                lastpkt=now
            if len(msg)%3==0:
                print(convert.ternary2string(msg))
    

sniff(iface='eth1', prn = recv)
