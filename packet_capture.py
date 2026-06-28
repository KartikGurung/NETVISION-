from scapy.all import sniff
from scapy.layers.inet import IP

class PacketCapture:
    def __init__(self):
        self.running = False
    
    def process_packet(self, packet):
        if IP in packet:
            print(
                f"{packet[IP].src}--->{packet[IP].dst}\n"
                f"{packet.summary()}"
            )
    def start(self):
        self.running = True
        sniff(
            prn = self.process_packet,
            store = False
        )
    