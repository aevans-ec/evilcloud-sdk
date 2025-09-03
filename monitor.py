import datetime
import logging

class EvilCloudMonitor:
    def __init__(self):
        self.audit_logs = []
        logging.basicConfig(level=logging.INFO)

    def log_event(self, user: str, action: str, resource: str):
        event = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "user": user,
            "action": action,
            "resource": resource
        }
        self.audit_logs.append(event)
        logging.info(f"AUDIT: {event}")

    def get_logs(self, limit: int = 10):
        return self.audit_logs[-limit:]

    def export_logs(self, filename: str):
        with open(filename, "w") as f:
            for log in self.audit_logs:
                f.write(str(log) + "\n")
