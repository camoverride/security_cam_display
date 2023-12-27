# Image Display

Display recent images from a folder to the screen.


## Setup

Install the python requirements: `pip install -r requirements.txt`.


## Run

- `nohup python front_end.py &`
- Set the display: `export DISPLAY=:0`
- Show full-screen in Firefox: `firefox --kiosk --private-window http://127.0.0.1:123`
- Or Chromium: `chromium-browser --kiosk http://127.0.0.1:1234`

If there is no local archive, it needs to be updated. Run: `nohup update_archive.py &`

**TODO**: this should be run as a standalone file: `file://display.html` in the browser!
