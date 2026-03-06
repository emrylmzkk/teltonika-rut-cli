import subprocess
import platform
import time
import socket

class RouterHealthService:

    def __init__(self, host = "192.168.1.1"):
        self.host = host

    def _check_user_platform(self):

        user_platform = platform.system().lower()

        match user_platform:

            case "windows" :
                return ["ping", "-n", "1", self.host]
                

            case _:
                return ["ping", "-c", "1", self.host]

    def ping_router_ports(self, port):
        
        try:
            with socket.create_connection((self.host, port), timeout=3):
                return True
        except:
            return False
        
    


    def ping_router(self, retries=5, delay=4):

        platform_command = self._check_user_platform()

        for i in range(1, retries + 1):

            try:

                result = subprocess.run(
                    platform_command,
                    capture_output=True,
                    text=True
                ) 

                if result.returncode == 0:
                    return True
                
                print(f"Ping failed. Retry {i} / {retries}")

                time.sleep(delay)

            except Exception as e:
                return False
            
        return False
    
    def check_router_health(self):

        return {
            "ping" : self.ping_router(),
            "ssh" : self.ping_router_ports(22),
            "http" : self.ping_router_ports(80),
            "https" : self.ping_router_ports(443)
        }
    
