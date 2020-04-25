#################
#   libraris    #
#################
import scapy.all as scapy

def scan(ip):
    ARPRequest = scapy.ARP(pdst=ip)
    Broadcast = scapy.Ether()
    scapy.ls(scapy.Ether())

#scan(ip/rang)
scan("10.0.2.4/24")
