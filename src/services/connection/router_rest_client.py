import requests
from router_app_config import ROUTER_HOST, REQUEST_TIMEOUT_MS

class RouterRestClient:

    def __init__(self):
        self.base_url = ROUTER_HOST
        self.session = requests.Session()
        self.timeout = REQUEST_TIMEOUT_MS
        

    def post(self, endpoint, data=None):

        url = f"{self.base_url}{endpoint}"

        res = self.session.post(
            url,
            json=data,
            timeout=self.timeout
        )

        res.raise_for_status()

        return res.json()
