"""
Security Framework Example - Educational Version

Purpose:
This code simulates a basic security testing framework that students can use to understand
the fundamentals of vulnerability scanning and exploitation. It demonstrates:
1. How vulnerability scanners work at a basic level
2. The relationship between ports and vulnerabilities
3. How security tools report and exploit vulnerabilities
4. Basic security assessment workflow

This is a simplified simulation for educational purposes and doesn't perform actual scanning
or exploitation.
"""

import time
import random
import logging
from dataclasses import dataclass
from typing import List, Dict

# Set up basic logging to see what's happening
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@dataclass
class Vulnerability:
    """Represents a security vulnerability with its basic properties"""
    name: str           # Name of the vulnerability
    description: str    # What the vulnerability is about
    severity: str       # How dangerous it is (Low/Medium/High/Critical)
    affected_ports: List[int]  # Which ports this vulnerability affects

@dataclass
class ExploitModule:
    """Represents a tool to exploit a specific vulnerability"""
    name: str           # Name of the exploit
    target_vulnerability: str  # Which vulnerability it targets
    success_rate: float       # How likely it is to work (0.0 to 1.0)

class SimpleSecurityScanner:
    def __init__(self):
        # Initialize with some example vulnerabilities and exploits
        self.vulnerabilities = [
            Vulnerability(
                name="FTP Anonymous Access",
                description="FTP server allows login without password",
                severity="Medium",
                affected_ports=[21]
            ),
            Vulnerability(
                name="Web Server Vulnerability",
                description="Old version of web server with known issues",
                severity="High",
                affected_ports=[80, 443]
            )
        ]
        
        self.exploits = [
            ExploitModule(
                name="ftp_anonymous_exploit",
                target_vulnerability="FTP Anonymous Access",
                success_rate=0.7
            ),
            ExploitModule(
                name="web_server_exploit",
                target_vulnerability="Web Server Vulnerability",
                success_rate=0.6
            )
        ]
        
        # Store scan results for each IP address
        self.scan_results: Dict[str, List[Vulnerability]] = {}

    def scan_target(self, target_ip: str):
        """
        Simulate scanning a target IP address for vulnerabilities.
        In real life, this would actually connect to the target.
        """
        print(f"\nScanning target: {target_ip}")
        found_vulnerabilities = []
        
        # Check common ports
        common_ports = [21, 22, 80, 443, 3306, 8080]
        for port in common_ports:
            print(f"Checking port {port}...")
            
            # Simulate port scanning (randomly determine if port is open)
            if random.random() < 0.5:  # 50% chance port is "open"
                print(f"Port {port} is open!")
                
                # Check if any known vulnerabilities affect this port
                for vuln in self.vulnerabilities:
                    if port in vuln.affected_ports:
                        found_vulnerabilities.append(vuln)
                        print(f"Found vulnerability: {vuln.name}")
        
        self.scan_results[target_ip] = found_vulnerabilities
        return found_vulnerabilities

    def try_exploit(self, target_ip: str, vulnerability_name: str) -> bool:
        """
        Simulate attempting to exploit a vulnerability.
        Returns True if exploitation was "successful".
        """
        # Find the matching exploit
        exploit = next(
            (e for e in self.exploits if e.target_vulnerability == vulnerability_name),
            None
        )
        
        if not exploit:
            print(f"No exploit available for {vulnerability_name}")
            return False
            
        print(f"\nTrying to exploit {vulnerability_name}...")
        time.sleep(1)  # Simulate some work being done
        
        # Simulate success/failure based on the exploit's success rate
        success = random.random() < exploit.success_rate
        if success:
            print("Exploit successful!")
        else:
            print("Exploit failed!")
            
        return success

    def generate_report(self, target_ip: str) -> str:
        """Create a simple security report for the target"""
        vulnerabilities = self.scan_results.get(target_ip, [])
        
        report = f"\nSecurity Report for {target_ip}\n"
        report += "=" * 40 + "\n"
        
        if not vulnerabilities:
            report += "No vulnerabilities found.\n"
            return report
        
        report += f"Found {len(vulnerabilities)} vulnerabilities:\n\n"
        for vuln in vulnerabilities:
            report += f"- {vuln.name} (Severity: {vuln.severity})\n"
            report += f"  Description: {vuln.description}\n"
            report += f"  Affected Ports: {vuln.affected_ports}\n\n"
        
        return report

def run_demo():
    """Demonstrate how the security scanner works"""
    scanner = SimpleSecurityScanner()
    target = "192.168.1.100"  # Example IP address
    
    print("=== Security Scanner Demo ===")
    
    # Step 1: Scan for vulnerabilities
    print("\nStep 1: Scanning for vulnerabilities...")
    found_vulns = scanner.scan_target(target)
    
    # Step 2: Show the report
    print("\nStep 2: Generating security report...")
    report = scanner.generate_report(target)
    print(report)
    
    # Step 3: Try to exploit found vulnerabilities
    if found_vulns:
        print("\nStep 3: Attempting to exploit vulnerabilities...")
        for vuln in found_vulns:
            scanner.try_exploit(target, vuln.name)

if __name__ == "__main__":
    run_demo() 