import os
import time
import logging



ARCHIVE_CHECK_INTERVAL = 10 # seconds
ARCHIVE_REMOTE_LOCATION = "cam@cam-machine.local:~/security_cam_display/static/archive"
PASSWORD = "a"

def update_archive():
    logging.warning("Updating archive!")
    try:
        # Get the files
        os.system(f"sshpass -p {PASSWORD} scp -r {ARCHIVE_REMOTE_LOCATION} static/archive")

    except Exception as e:
        logging.warn(e)
    
    time.sleep(ARCHIVE_CHECK_INTERVAL)


while True:
    update_archive()
