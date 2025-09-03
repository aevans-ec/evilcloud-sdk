from auth import EvilCloudAuth
from storage import EvilCloudStorage
from monitor import EvilCloudMonitor

if __name__ == "__main__":
    # Initialize
    auth = EvilCloudAuth("client123", "supersecret")
    storage = EvilCloudStorage(auth)
    monitor = EvilCloudMonitor()

    # Upload
    file = storage.upload_file("report.txt", "Confidential EvilCloud report")
    monitor.log_event("alice.evans", "upload", file["file_id"])

    # List files
    files = storage.list_files()
    print("Files:", files)

    # Download
    fid = list(files.keys())[0]
    content = storage.download_file(fid)
    print("Downloaded content:", content)

    # Logs
    print("Recent logs:")
    for log in monitor.get_logs():
        print(log)
