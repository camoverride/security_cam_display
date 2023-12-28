import os
import time
import logging



logging.basicConfig(level=logging.DEBUG)

ARCHIVE_CHECK_INTERVAL = 10 # seconds
ARCHIVE_REMOTE_LOCATION = "cam@cam-machine.local:/home/cam/Desktop/whisper_server/archive"
ARCHIVE_LOCAL_LOCATION_BASE_PATH = "/home/pi/Desktop"
PASSWORD = "a"


def update_archive():
    logging.debug("Updating archive!")
    try:
        # Get the files
        os.system(f"sshpass -p {PASSWORD} scp -r {ARCHIVE_REMOTE_LOCATION} {ARCHIVE_LOCAL_LOCATION_BASE_PATH}")

    except Exception as e:
        logging.warn(e)
    
    time.sleep(ARCHIVE_CHECK_INTERVAL)


while True:
    update_archive()
