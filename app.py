#Pi-Web-Dashboard

import gpiozero, psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	CPU_Temp = gpiozero.CPUTemperature()
	CPU_Usage = psutil.cpu_percent(interval=1)
	RAM = psutil.virtual_memory()
	mymessage = ("TEST 1")
	return render_template("index.html", message=mymessage, CPU_T=f"CPU Temp: {CPU_Temp.temperature:.1f}\u00B0C",CPU_U=f"CPU Usage: {CPU_Usage}%", RAM=f"RAM Usage: {RAM.percent}%")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
