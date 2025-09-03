import os
import json
from typing import Dict, Any

class EvilCloudStorage:
    def __init__(self, auth):
        self.auth = auth
        self.files: Dict[str, Any] = {}

    def upload_file(self, filename: str, content: str) -> Dict[str, str]:
        token = self.auth.get_token()
        file_id = f"ECF-{hash(filename) & 0xfffffff}"
        self.files[file_id] = {"name": filename, "content": content}
        return {"file_id": file_id, "status": "uploaded"}

    def download_file(self, file_id: str) -> str:
        if file_id not in self.files:
            raise ValueError("File not found in EvilCloud")
        return self.files[file_id]["content"]

    def list_files(self) -> Dict[str, str]:
        return {fid: meta["name"] for fid, meta in self.files.items()}

    def delete_file(self, file_id: str) -> bool:
        if file_id in self.files:
            del self.files[file_id]
            return True
        return False
