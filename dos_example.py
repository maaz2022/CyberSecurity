# dos_example.py
import time
import threading
from collections import defaultdict
import queue
from datetime import datetime, timedelta

class Server:
    def __init__(self, capacity=100, rate_limit=10):
        self.capacity = capacity  # Maximum concurrent connections
        self.current_connections = 0
        self.rate_limit = rate_limit  # Requests per second per IP
        self.request_queue = queue.Queue(maxsize=capacity)
        self.ip_tracking = defaultdict(list)
        self.blacklist = set()
        
    def handle_request(self, ip_address, request_data):
        # Check if IP is blacklisted
        if ip_address in self.blacklist:
            return f"Error: IP {ip_address} is blacklisted"
            
        # Rate limiting check
        current_time = datetime.now()
        self.ip_tracking[ip_address] = [
            timestamp for timestamp in self.ip_tracking[ip_address] 
            if current_time - timestamp < timedelta(seconds=1)
        ]
        
        # Add current request timestamp
        self.ip_tracking[ip_address].append(current_time)
        
        # Check rate limit
        if len(self.ip_tracking[ip_address]) > self.rate_limit:
            self.blacklist.add(ip_address)
            return f"Error: Rate limit exceeded. IP {ip_address} has been blacklisted"
        
        # Check server capacity
        if self.current_connections >= self.capacity:
            return "Error: Server at maximum capacity"
            
        try:
            # Process the request
            self.current_connections += 1
            self.request_queue.put(request_data, timeout=1)
            time.sleep(0.1)  # Simulate request processing
            return f"Request from {ip_address} processed successfully"
        finally:
            self.current_connections -= 1

class NormalClient:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        
    def send_request(self, server, request_data):
        response = server.handle_request(self.ip_address, request_data)
        print(f"Normal Client {self.ip_address}: {response}")

class DoSAttacker:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        
    def flood_attack(self, server, num_requests):
        print(f"\nAttacker {self.ip_address} starting flood attack...")
        for i in range(num_requests):
            response = server.handle_request(self.ip_address, f"malicious_data_{i}")
            print(f"Attacker {self.ip_address}: {response}")
            time.sleep(0.1)  # Small delay to make output readable

def demonstrate_dos_attack():
    # Initialize server with protection mechanisms
    server = Server(capacity=100, rate_limit=10)
    
    # Create normal clients
    normal_client1 = NormalClient("192.168.1.1")
    normal_client2 = NormalClient("192.168.1.2")
    
    # Create attacker
    attacker = DoSAttacker("10.0.0.1")
    
    print("Scenario 1: Normal Traffic")
    print("--------------------------")
    # Simulate normal traffic
    for _ in range(5):
        normal_client1.send_request(server, "legitimate_request")
        normal_client2.send_request(server, "legitimate_request")
        time.sleep(0.2)
    
    print("\nScenario 2: DoS Attack")
    print("----------------------")
    # Start DoS attack in a separate thread
    attack_thread = threading.Thread(
        target=attacker.flood_attack, 
        args=(server, 20)
    )
    attack_thread.start()
    
    # Continue normal client operations during attack
    for _ in range(5):
        normal_client1.send_request(server, "legitimate_request")
        time.sleep(0.3)
    
    attack_thread.join()
    
    print("\nScenario 3: Post-Attack Normal Traffic")
    print("-------------------------------------")
    # Show that legitimate clients can still operate
    for _ in range(3):
        normal_client1.send_request(server, "legitimate_request")
        normal_client2.send_request(server, "legitimate_request")
        time.sleep(0.2)

if __name__ == "__main__":
    demonstrate_dos_attack()