
import time
from src.services.connection.router_ssh_client import RouterSshClient

class RelayService:

    def __init__(self, host ="192.168.1.1"):
        self.host = host
        #self.ssh = RouterSshClient(host)


    def reboot_relay(self, relay="relay0", duration=3):

        close_cmd = f"ubus call ioman.relay.{relay} update '{{\"state\":\"closed\"}}'"
        open_cmd = f"ubus call ioman.relay.{relay} update '{{\"state\":\"open\"}}'"

        with RouterSshClient(self.host) as ssh:
            
            ssh.exec_command_to_root(close_cmd)

            time.sleep(duration)

            result = ssh.exec_command_to_root(open_cmd)
            
        #result = self.ssh.exec_command_to_root(command)

        return result