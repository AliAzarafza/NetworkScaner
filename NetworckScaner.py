#################
#   libraris    #
#################
import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)


#scan(ip/rang)
scan("10.0.2.4/24")
