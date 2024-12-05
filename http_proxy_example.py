from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import logging
from urllib.parse import urlparse
from datetime import datetime

# Configure logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ProxyHandler(BaseHTTPRequestHandler):
    """
    HTTP Proxy Handler Class
    Handles incoming HTTP requests and forwards them to destination servers
    
    Limitations:
    - Only supports HTTP (not HTTPS)
    - Basic error handling
    - No authentication
    - No caching
    """
    
    # Define blocked domains (for content filtering)
    BLOCKED_DOMAINS = {'facebook.com', 'twitter.com', 'instagram.com'}
    
    # Store access logs
    access_log = []

    def do_GET(self):
        """
        Handle GET requests
        
        Flow:
        1. Parse incoming request URL
        2. Check if domain is blocked
        3. Forward request to destination
        4. Return response to client
        
        Note: This implementation is for educational purposes
        and lacks many production-ready features
        """
        try:
            # Log request details for debugging
            logging.info(f"Received request for: {self.path}")
            
            # Construct proper URL
            url = self.path
            if not url.startswith(('http://', 'https://')):
                url = f'http://{self.headers["Host"]}{url}'
            
            logging.info(f"Processed URL: {url}")
            
            # Parse URL for domain checking
            parsed_url = urlparse(url)
            
            # Check for blocked domains
            if self.is_blocked_domain(parsed_url.netloc):
                logging.warning(f"Blocked access to: {parsed_url.netloc}")
                self.send_blocked_response()
                return
            
            # Forward request to destination
            logging.info(f"Forwarding request to: {url}")
            response = urllib.request.urlopen(url, timeout=10)
            
            # Send response back to client
            self.send_response(response.status)
            for header, value in response.getheaders():
                self.send_header(header, value)
            self.end_headers()
            
            # Forward response body
            self.wfile.write(response.read())
            
        except Exception as e:
            logging.error(f"Error processing request: {str(e)}")
            self.send_error(500, f"Proxy Error: {str(e)}")

    def is_blocked_domain(self, domain):
        """
        Check if the requested domain is in the list of blocked domains.
        Returns True if the domain is blocked, False otherwise.
        """
        return any(blocked in domain.lower() for blocked in self.BLOCKED_DOMAINS)

    def send_blocked_response(self):
        """
        Sends a 403 Forbidden response to the client for blocked domains.
        Includes a custom HTML message explaining the block.
        """
        self.send_response(403)  # HTTP status code for Forbidden
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # HTML content for the blocked message
        blocked_message = """
        <html>
            <body>
                <h1>Access Denied</h1>
                <p>This website has been blocked by the proxy server.</p>
            </body>
        </html>
        """
        # Write the message to the response
        self.wfile.write(blocked_message.encode())

    def log_request_details(self):
        """
        Logs details of the client's request, including IP address, timestamp, and user agent.
        Stores the data in the access log.
        """
        client_ip = self.client_address[0]  # Get the IP address of the client
        timestamp = datetime.now()         # Current time of the request
        request_line = self.requestline    # The full request line (e.g., GET / HTTP/1.1)
        
        # Capture and log the details of the request
        log_entry = {
            'timestamp': timestamp,
            'client_ip': client_ip,
            'request': request_line,
            'user_agent': self.headers.get('User-Agent', 'Unknown')
        }
        
        # Store the log entry in the class's access log
        ProxyHandler.access_log.append(log_entry)
        logging.info(f"Request from {client_ip}: {request_line}")

class MonitoringInterface:
    """
    Provides functionalities to monitor and analyze logged requests.
    Includes printing access logs and generating basic statistics.
    """
    @staticmethod
    def print_access_log():
        """
        Prints all logged requests to the console in a readable format.
        """
        print("\nAccess Log:")
        print("-" * 50)
        for entry in ProxyHandler.access_log:
            print(f"Time: {entry['timestamp']}")
            print(f"Client IP: {entry['client_ip']}")
            print(f"Request: {entry['request']}")
            print(f"User Agent: {entry['user_agent']}")
            print("-" * 50)
    
    @staticmethod
    def get_statistics():
        """
        Computes basic statistics about the requests logged by the proxy.
        Returns the statistics as a formatted string.
        """
        if not ProxyHandler.access_log:
            return "No requests logged yet."
        
        total_requests = len(ProxyHandler.access_log)
        unique_ips = len(set(entry['client_ip'] for entry in ProxyHandler.access_log))
        
        return f"""
        Statistics:
        - Total Requests: {total_requests}
        - Unique Client IPs: {unique_ips}
        """

def run_proxy(port=8080):
    """
    Starts the proxy server on the specified port.
    Provides options to monitor and stop the server gracefully.
    """
    try:
        # Create the proxy server instance
        proxy_server = HTTPServer(('', port), ProxyHandler)
        print(f"Starting proxy server on port {port}")
        print("Press Ctrl+C to stop")
        
        # Start serving requests
        proxy_server.serve_forever()
        
    except KeyboardInterrupt:
        # Handle shutdown gracefully when user interrupts
        print("\nShutting down proxy server")
        proxy_server.shutdown()
        
        # Display monitoring data after shutdown
        monitor = MonitoringInterface()
        monitor.print_access_log()
        print(monitor.get_statistics())

if __name__ == "__main__":
    # Start the proxy server
    run_proxy()
