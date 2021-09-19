import socket 
from pprint import pprint

# I myself am in the stage of creating a python packet parser/sniffer and in my research I found that, 
# to be able parse all the incoming packets like TCP, ICMP, UDP, ARP ..etc., you must not use the below 
# socket type because socket.IPPROTO_IP gives out only IP packets and is a dummy protocol
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)


s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))


print(s)

value = (s.recvfrom(65565)) #65565 -> 2^16 -> 2 bytes
pprint((value))
f = open("socker_recvform_param_65565.txt", "a")
f.write(value[0])
f.close()



# while True:
#  print(s.recvfrom(65565)) #65565 -> 2^16 -> 2 bytes
 
