from src.services.router_health_service import RouterHealthService
from src.services.connection.router_ssh_client import RouterSshClient

class RouterFirmwareProcess:

    def __init__(self):
        self.health_service = RouterHealthService()
        self.ssh_client = RouterSshClient(host="192.168.1.1")

    def update_router_firmware(self, local_path: str):
        
        with self.ssh_client:

            sftp_result = self.ssh_client.upload_file(local_path, "/tmp/firmware.bin")

            if not sftp_result:
                return False
            
            self.ssh_client.exec_command_to_root(
                "sysupgrade /tmp/firmware.bin"
            )

            return True

    def upload_backup(self, local_path : str):

        with self.ssh_client:

            sftp_result = self.ssh_client.upload_file(local_path, "/tmp/router_backup.tar.gz")

            if sftp_result is False:
                return False
            
            self.ssh_client.exec_command_to_root(
                "sysupgrade -r /tmp/router_backup.tar.gz"
            )

            return True
    