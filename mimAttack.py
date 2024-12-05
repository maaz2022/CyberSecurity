Python Example: Network Packet Sniffing
Below is a script to sniff packets on a network:
def sniff_packets_simulated():
    # Simulated packets for demonstration purposes
    simulated_packets = [
        {"src": "192.168.1.1", "dst": "192.168.1.100", "data": "Hello, this is packet 1"},
        {"src": "192.168.1.2", "dst": "192.168.1.101", "data": "This is packet 2 for demo"},
        {"src": "10.0.0.1", "dst": "10.0.0.5", "data": "Packet 3: Learning is fun!"},
        {"src": "172.16.0.1", "dst": "172.16.0.100", "data": "Simulated packet 4"},
    ]

    print("Simulated Packet Sniffing")
    print("Displaying packets for educational purposes:\n")

    # Process each simulated packet
    for i, packet in enumerate(simulated_packets, start=1):
        print(f"Packet {i}:")
        print(f"  Source: {packet['src']}")
        print(f"  Destination: {packet['dst']}")
        print(f"  Data: {packet['data']}\n")

# Run the simulated sniffer
sniff_packets_simulated()

