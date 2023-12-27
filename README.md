# Image Display

Display recent images from a folder to the screen.


## Setup

Install the python requirements: `pip install -r requirements.txt`.


## Run

Start manually:
- `nohup python front_end.py &`
- Set the display: `export DISPLAY=:0`
- Show full-screen in Firefox: `firefox --kiosk --private-window http://127.0.0.1:123`
- Or Chromium: `chromium-browser --kiosk http://127.0.0.1:1234`

If there is no local archive, it needs to be updated. Run: `nohup python update_archive.py &`

Or, start with systemd:
This will start the program when the computer starts and revive it when it dies. Copy the contents of `front_end.service` to `/etc/systemd/system/front_end.service` (via `sudo vim /etc/systemd/system/front_end.service`).

Start the service using the commands below.

- `sudo systemctl daemon-reload`
- Start it on boot: `sudo systemctl enable recordingloop.service` 
- Start it right now: `sudo systemctl start recordingloop.service`
- Stop it right now: `sudo systemctl stop recordingloop.service`
- Get logs: `sudo journalctl -u recordingloop | tail`


**TODO**: this should be run as a standalone file: `file://display.html` in the browser!

## About

In `front_end.py` edit `TRACKED_CAMERAS` to add or remove cameras from the display.
