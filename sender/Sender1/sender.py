from scapy.contrib import coap
from scapy.all import IP, UDP,send,sr1
from time import sleep
import random
import convert
import argparse



parser = argparse.ArgumentParser(description='Send a secret Message via reset Covert Channel')

parser.add_argument('--short', action='store', type=float, default=0.2, help='Short waiting time')
parser.add_argument('--med', action='store', type=float, default=0.4, help='Medium waiting time')
parser.add_argument('--long', action='store', type=float, default=0.6, help='Long waiting time')

parser.add_argument('--msg', action='store', default="Secret", help='String to send')

args = parser.parse_args()
mid=random.randint(1000,50000)
short = args.short
med = args.med
long = args.long

message = args.msg
res = convert.string2ternary(message)

print("Sending: " + message)
print("Encoded: " + str(res))

pk1 = IP(dst="10.10.0.2",src="10.10.0.3")/UDP(dport=5683, sport=34865)/coap.CoAP(type=0,msg_id=mid,code=0)
send(pk1)

for i in res:
    mid=random.randint(1000,50000)
    if i == 0:
        sleep(short)
    elif i == 1:
        sleep(med)
    else:
        sleep(long)
    pk1 = IP(dst="10.10.0.2",src="10.10.0.3")/UDP(dport=5683, sport=34865)/coap.CoAP(type=0,msg_id=mid,code=0)
    send(pk1)
print(res)
