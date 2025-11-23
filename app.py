#Pi-Web-Dashboard

import gpiozero
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	CPU_Temp = gpiozero.CPUTemperature()
	CPU_Temp = round(CPU_Temp.temperature, 2)
	mymessage = ("CPU Temp = " + str(CPU_Temp) + "\u00b0C")
	return render_template("index.html", message=mymessage)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
