import time

session_timeout = 1800  # Session expires after 30 minutes
start_time = time.time()

if time.time() - start_time > session_timeout:
    print("Session expired")
