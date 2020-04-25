#################
#   libraris    #
#################
import scapy.all as scapy

def scan(ip):
    ARPRequest = scapy.ARP(pdst = ip)
    Broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    ARPRequestBroadcast = Broadcast/ARPRequest
    answered, unanswered = scapy.srp(ARPRequestBroadcast, timeout=5)
    print(answered.summary())



#scan(ip/rang)
scan("10.0.2.4/24")
