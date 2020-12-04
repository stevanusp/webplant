# Imports
from flask import *
import json
import queue
import serial
import time
import threading
# GLOBALS
arduinoPortLinux = '/dev/ttyACM0'
arduinoPortWindows = 'COM3'
host = '0.0.0.0'  # == localhost
webPort = 8080
app = Flask(__name__)
q = queue.Queue()
# Data Containers
humidity = []
temperature = []
soilMoisture = []
# Routes


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/update", methods=['GET'])
def updateData():
    while not q.empty():
        humidity.append(q.get())
        temperature.append(q.get())
        soilMoisture.append(q.get())
    result = [
        humidity[len(humidity)-1],
        temperature[len(temperature)-1],
        soilMoisture[len(soilMoisture)-1]
    ]
    return jsonify(result)


def dataCollector():
    data = getDataParsed()
    # put data in queue
    q.put(float(data["humidity"]))
    q.put(float(data["temperature"]))
    q.put(int(data["soilMoisture"]))


def getDataParsed():
    """
    Return parsed json of data from sensors in dictionary form
    """
    serialConsole.flush()
    rawData = serialConsole.readline().decode("utf-8").rstrip()
    parsedJson = json.loads(rawData)
    return parsedJson


# Main
if __name__ == '__main__':
    serialConsole = serial.Serial(arduinoPortWindows, 9600, timeout=5)
    x = threading.Thread(target=dataCollector)
    x.start()
    app.run(host, webPort)
