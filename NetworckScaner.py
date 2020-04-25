#################
#   libraris    #
#################
import scapy.all as scapy

def scan(ip):
    ARPRequest = scapy.ARP(pdst = ip)
    Broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    ARPRequestBroadcast = Broadcast/ARPRequest
    answeredList = scapy.srp(ARPRequestBroadcast, timeout=5, verbose=False)[0]
    print('___________________________________________\n ip\t\t\tMAC adress\n-----------------------------------')
    for element in answeredList:
        print(element[1].psrc'\t\t'element[1].hwsrc)



#scan(ip/rang)
scan("10.0.2.4/24")
