import os
import time
from threading import Thread

from flask import Flask, render_template



ARCHIVE = "/home/cam/Desktop/whisper_server/archive/"
UPDATE_INTERVAL = 5 # seconds
MAX_FILES = 16 # Maximum number of face images to be copied. Should be greater than or equal to the # needed.


# Set up Flask
app = Flask(__name__)

# Render the front-end
@app.route("/")
def index():
    return render_template("display.html")

# Update files in `static/archive`
def get_new_files():
    while True:
        print("UPDATING archive contents!")
        files = os.listdir(ARCHIVE)
        files_new_to_old = list(reversed(sorted(files)))
        
        # Rename files as 1.jpg, 2.jpg etc
        for index, filename in enumerate(files_new_to_old[:MAX_FILES]):
            os.system(f"mv {ARCHIVE}/{filename} static/archive/{index}.jpg")

        time.sleep(UPDATE_INTERVAL)


t = Thread(target=get_new_files)
t.start()
