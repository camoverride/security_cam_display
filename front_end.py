import os
import time
from threading import Thread
from flask import Flask, render_template
import logging



ARCHIVE_LOCAL_LOCATION = "/home/cam/Desktop/whisper_server/archive" # Upstairs setting
ARCHIVE_LOCAL_LOCATION = "/home/pi/Desktop/archive" # Downstairs setting
UPDATE_INTERVAL = 5 # seconds
MAX_FILES = 16 # Maximum number of face images to be copied. Should be greater than or equal to the # needed.
TRACKED_CAMERAS = ["pi1", "pi2", "pi4", "pi5", "cam-machine"] # Upstairs setting
TRACKED_CAMERAS = "all" # Downstairs setting


def get_suffix(filename):
    if TRACKED_CAMERAS == "all":
        return True

    suffix = filename.split("_")[-1].split(".")[0]
    if suffix in TRACKED_CAMERAS:
        return True
    else:
        return False


# Set up Flask
app = Flask(__name__)

# Render the front-end
@app.route("/")
def index():
    return render_template("display.html")

# Update files in `static/archive`
def get_new_files():
    while True:
        try:
            logging.debug("UPDATING archive contents!")
            files = os.listdir(ARCHIVE_LOCAL_LOCATION)
            files_new_to_old = list(reversed(sorted(files)))
            print(files_new_to_old)

            # Copy and rename files as 1.jpg, 2.jpg etc.
            for index, filename in enumerate(files_new_to_old[:MAX_FILES]):
                print(filename)
                tracked_camera = get_suffix(filename)
                print(tracked_camera)
                if tracked_camera:
                    cmd = f"cp {ARCHIVE_LOCAL_LOCATION}/{filename} static/archive/{index}.jpg"
                    print(cmd)
                    os.system(cmd)

            time.sleep(UPDATE_INTERVAL)

        except Exception as e:
            logging.warning(e)


# Start the file update thread
t = Thread(target=get_new_files)
t .start()

# Start the app
app.run(port=1234)
