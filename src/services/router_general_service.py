from src.services.connection.router_ssh_client import RouterSshClient
class RouterGeneralService:
    

    def __init__(self, host="192.168.1.1"):
        self.host = host
        self.ssh_client = RouterSshClient(host)


    def get_router_info(self):

        command = "ubus call system board"

        with self.ssh_client:
            result = self.ssh_client.exec_command_to_root(command)
        
        return result
    

router_general_service = RouterGeneralService()
        