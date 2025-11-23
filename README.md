# Raspberry Pi CPU Dashboard

A simple Flask web app that runs on a Raspberry Pi and shows basic system stats in a local browser.

Currently displays:
- CPU temperature
- CPU usage
- RAM usage

## Requirements

- Raspberry Pi (tested on Raspberry Pi 4 Model B)
- Raspberry Pi OS with Python 3 installed
- Network connection (so you can open the page from another device)

Python packages (also listed in `requirements.txt`):
- Flask  
- gpiozero  
- psutil  

## Setup

1. Clone the repository onto your Pi:

   ```bash
   git clone https://github.com/<your-username>/pi-web-dashboard.git
   cd pi-web-dashboard
   ```

2. Install the dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

## Running the app

1. Start the Flask server:

   ```bash
   python3 app.py
   ```

2. Find your Pi's IP address:

   ```bash
   hostname -I
   ```

3. On another device on the same network (phone, laptop, etc.), open a browser and go to:

   ```
   http://<pi-ip>:5000
   ```

You should now see the dashboard with CPU temperature, CPU usage, and RAM usage.

## Project structure

```
pi-web-dashboard/
├── app.py              # Flask app and system metrics logic
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── templates/
    └── index.html      # HTML template for the dashboard
```

## Possible Future Ideas

- Show disk usage  
- Show system uptime  
- Add nicer styling and layout  
- Add a `/status` page with raw JSON  
