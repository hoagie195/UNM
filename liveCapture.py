import pyshark,time
from ipInfo import IP
from kmeanAI import KMEAN

from registeredIPS import registeredIPS 
class packetCapture:
    def __init__(self):
        self.newIP = True
        self.packet_list = []
        self.registeredIPS = registeredIPS()
        self.capture = pyshark.LiveCapture(interface="Wi-Fi", bpf_filter="not udp")
        self.timer = time.perf_counter()
        super().__init__()
        
    def start(self):
        for packet in self.capture.sniff_continuously():
            self.packet_list.append(packet)
            if len(self.registeredIPS.ips) != 0 and 'IP' in packet:
                for ip in self.registeredIPS.ips:
                    if ip.ipsrc == packet.ip.src:
                        self.newIP = False
                        ip.totalNetworkTraffic += 1
                        self.registeredIPS.updateIPSInfo(packet.ip.dst)
                        break
            if self.newIP == True and 'IP' in packet:
                self.registeredIPS.ips.append(IP(packet.ip.src))
                self.registeredIPS.updateIPSInfo(packet.ip.dst)
            if time.perf_counter() - self.timer > 300:
                self.registeredIPS.updateIPSTime(time.perf_counter() - self.timer)
                for ip in self.registeredIPS.ips:
                    print("Average data usuage of " + str(ip.ipsrc) + " in the past five minutes: " + str(ip.averageNetworkTraffic) + " traffic per second")
                self.timer = time.perf_counter()
            if time.perf_counter() - self.timer > 400:
                KMEAN(self.registeredIPS).predict()
            self.newIP = True