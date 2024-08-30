from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

# Function to process and display packet information
def process_packet(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        # Extract source and destination IP addresses
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto  # Protocol number (6 for TCP, 17 for UDP)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Determine protocol name
        proto_name = "Unknown"
        if packet.haslayer(TCP):
            proto_name = "TCP"
        elif packet.haslayer(UDP):
            proto_name = "UDP"

        # Display relevant information
        print(f"[{timestamp}] {proto_name} Packet: {src_ip} -> {dst_ip}")

        # Extract and display payload data if available
        payload = bytes(packet[TCP].payload) if packet.haslayer(TCP) else bytes(packet[UDP].payload)
        if payload:
            print(f"Payload: {payload[:50]}...")  # Display first 50 bytes of payload for brevity

# Main function to start packet sniffing
def main():
    print("Packet Sniffer is running... Press Ctrl+C to stop.")
    # Capture packets on all interfaces (adjust 'iface' to target specific interface if needed)
    sniff(prn=process_packet, filter="ip", store=False)

if __name__ == "__main__":
    main()
