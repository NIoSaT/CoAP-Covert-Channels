from scapy.contrib import coap
from scapy.all import IP, UDP,send,sr1
from time import sleep
import random
import convert
import argparse
import subprocess
import signal
import os


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

p=subprocess.Popen(["coap-client","-m", 'get', '-s','0', '-k', '10', 'coap+tcp://10.10.0.2/example_data'],shell=False)
for i in res:
    if i == 0:
        sleep(short)
    elif i ==1:
        sleep(med)
    elif i== 2:
        sleep(long)
    p.send_signal(signal.SIGKILL)
    p=subprocess.Popen(["coap-client","-m", 'get', '-s','0', '-k', '10', 'coap+tcp://10.10.0.2/example_data'],shell=False)

