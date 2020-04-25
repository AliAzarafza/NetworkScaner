#################
#   libraris    #
#################
import scapy.all as scapy


#ARP recust and its resalts
def scan(ip):
    ARPRequest = scapy.ARP(pdst = ip)
    Broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    ARPRequestBroadcast = Broadcast/ARPRequest
    answeredList = scapy.srp(ARPRequestBroadcast, timeout=5, verbose=False)[0]
    clientList = []
    for element in answeredList:
        clientDict = {"ip":element[1].psrc, "MAC":element[1].hwsrc}
        clientList.append(clientDict)
    return clientList

#show resalts
def printer(resaltsLIST):
    print('___________________________________________\n ip\t\t\tMAC adress\n-----------------------------------')
    for client in resaltsLIST:
        print(client["ip"] + '\t\t' + client["MAC"])


#scan(ip/rang)
scanResalt = scan("10.0.2.4/24")
printer(scanResalt)
