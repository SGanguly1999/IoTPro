from flask import Flask, render_template
import WristHealthBand
from coapSensorClient.publishCoAP import *

app = Flask(__name__)
device = WristHealthBand.WristHealthBand()
acc = device.acc
ali = device.alti
wei = device.weight
pulse = device.pulse
number = "7"
choice = 2
if choice == 1:
    import PublishData


@app.route('/')
def index():
    return render_template('index.html', number=number)


@app.route('/start_acc')
def start_acc():
    acc.start()
    if (choice == 1):
        PublishData.publishAccelerometerData(acc)
    else:
        coapPublishAccelerometer(acc)

    return "Accelerometer started"


@app.route('/stop_acc')
def stop_acc():
    acc.stop()
    return "Accelerometer stopped"


@app.route('/start_ali')
def start_ali():
    ali.start()
    if choice == 1:
        PublishData.publishAlimeterData(ali)
    else:
        coapPublishAlimeter(ali)
    return "Alimeter started"


@app.route('/stop_ali')
def stop_ali():
    ali.stop()
    return "Alimeter stopped"


@app.route('/start_weight')
def start_weight():
    wei.start()
    if choice == 1:
        PublishData.publishWeightSensorData(wei)
    else:
        coapPublishWeight(wei)
    return "Weight sensor started"


@app.route('/stop_weight')
def stop_weight():
    wei.stop()
    return "Weight sensor stopped"


@app.route('/start_pulse')
def start_pulse():
    pulse.start()
    if choice == 1:
        PublishData.publishPulseSensorData(pulse)
    else:
        coapPublishPulse(pulse)
    return "Pulse sensor started"


@app.route('/stop_pulse')
def stop_pulse():
    pulse.stop()
    return "Pulse sensor stopped"

@app.route('/start_device')
def start_device():
    device.start()
    if choice == 1:
        PublishData.publishWristHealthBandData(device)
    else:
        coapPublishWristBand(device)
    return "Device started"


@app.route('/stop_device')
def stop_device():
    device.stop()
    return "Device stopped"


if __name__ == '__main__':
    app.run()

