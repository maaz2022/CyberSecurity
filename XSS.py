import subprocess
import platform

def check_for_updates():
    if platform.system() == 'Windows':
        # Use a valid Windows command like 'dir'
        result = subprocess.run(['cmd', '/c', 'dir'], stdout=subprocess.PIPE)
    else:
        # Linux-specific command
        result = subprocess.run(['sudo', 'apt-get', 'update'], stdout=subprocess.PIPE)
    
    print(result.stdout.decode())

check_for_updates()
