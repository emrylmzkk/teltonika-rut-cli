import paramiko
import json
from typing import Optional, Dict, Any


class RouterSshClient:

    def __init__ (
            self, 
            host : str, 
            username : str = "root", 
            password: str = "Adminadmin.1",
            key_path: Optional[str] = None
        ):
        self.host = host
        self.username = username
        self.password = password
        self.key_path = key_path
        self.client = paramiko.SSHClient()


    def __enter__(self):
        self.connect_to_root()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.disconnect()



    def connect_to_root(self):
        try: 

            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            connect_kwargs = {
                "hostname" : self.host,
                "username" : self.username,
                "timeout" : 10
            }

            if self.key_path:
                connect_kwargs["key_filename"] = self.key_path
            else:
                connect_kwargs["password"] = self.password

            self.client.connect(**connect_kwargs)

        except Exception as e:
            raise

    def disconnect (self): 
        if self.client:
            self.client.close()


    def exec_command_to_root(self, command: str) -> Dict[str, Any]:

        if not self.client:
            self.connect_to_root()

        stdin, stdout, stderr = self.client.exec_command(command)
        error = stderr.read().decode().strip()
        output = stdout.read().decode().strip()

        if error:
            return {
                "success": False,
                "error" : error
            }
        
        try: 

            if (output):
                data = json.loads(output)
            else:
                data = {}

            return {
                "success" : True,
                "data" : data
            }


        except json.JSONDecodeError:
            return {
                "success" : False,
                "data" :  output
            }




    