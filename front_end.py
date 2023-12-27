import os
import time
from threading import Thread
from flask import Flask, render_template
import logging



ARCHIVE = "/home/cam/Desktop/whisper_server/archive/"
UPDATE_INTERVAL = 5 # seconds
MAX_FILES = 16 # Maximum number of face images to be copied. Should be greater than or equal to the # needed.
TRACKED_CAMERAS = ["pi1", "pi2", "pi4", "pi5", "cam-machine"]


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
            files = os.listdir(ARCHIVE)
            files_new_to_old = list(reversed(sorted(files)))
            
            # Copy and rename files as 1.jpg, 2.jpg etc.
            for index, filename in enumerate(files_new_to_old[:MAX_FILES]):
                suffix = filename.split("_")[-1].split(".")[0]
                if suffix in TRACKED_CAMERAS:
                    os.system(f"cp {ARCHIVE}/{filename} static/archive/{index}.jpg")

            time.sleep(UPDATE_INTERVAL)

        except Exception as e:
            logging.warning(e)


# Start the file update thread
t = Thread(target=get_new_files)
t.start()

# Start the app
app.run(port=1234)
