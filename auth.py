import os
import time
import hashlib
import hmac
import requests

class EvilCloudAuth:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.expiry = 0

    def _sign_request(self, payload: str) -> str:
        return hmac.new(
            self.client_secret.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()

    def login(self) -> str:
        """
        Simulate login to EvilCloud and retrieve access token
        """
        payload = f"{self.client_id}:{int(time.time())}"
        signature = self._sign_request(payload)

        # Fake API call
        response = {
            "access_token": hashlib.md5(signature.encode()).hexdigest(),
            "expires_in": 3600
        }
        self.token = response["access_token"]
        self.expiry = int(time.time()) + response["expires_in"]
        return self.token

    def get_token(self) -> str:
        if not self.token or time.time() > self.expiry:
            return self.login()
        return self.token
