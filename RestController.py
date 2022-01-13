from flask import Flask, render_template        # web framework
import WristHealthBand                          # tool prepraed using four sensors
from coapSensorClient.publishCoAP import *      # implemented CoAp for communication
from application_logging.logger import App_Logger # for logging

app = Flask(__name__)                           # flask app is created
device = WristHealthBand.WristHealthBand()      # WristleHealthBand instance is created  
acc = device.acc                                # Accelorometer instance is assigned
ali = device.alti                               # Alimeter instance is assigned
wei = device.weight                             # Weignt sensor instance is assigned
pulse = device.pulse                            # Pulse Sensor is assigned
number = "7"                                    # number is assigned
choice = 2                                      # choice is assigned to call particular route
logger = App_Logger()                           # logger object is created

if choice == 1:                 
    import PublishData                          # if choice=1 then PublishData is imported


@app.route('/')
def index():
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Application is Started!")
    return render_template('index.html', number=number)     # Home Page is rendered


@app.route('/start_acc')                                    # route to start accelorometer
def start_acc():                                            
    acc.start()                                             # accelorometer is started
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Accelerometer is asked to start!") 
    log_file.close()                                           
    if (choice == 1):                                       
        PublishData.publishAccelerometerData(acc)           # mqtt is used
    else:
        coapPublishAccelerometer(acc)                       # coapp is used
    return "Accelerometer started"


@app.route('/stop_acc')                                     # route to stop using accelorometer
def stop_acc():
    acc.stop()                                              # accelorometer is  stopped
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Accelerometer is asked to stop!")
    log_file.close() 
    return "Accelerometer stopped"


@app.route('/start_ali')                                           # route to  start alimeter
def start_ali():
    ali.start()                                                    # alimeter is started
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Alimeter is asked to start!")
    log_file.close() 
    if choice == 1:
        PublishData.publishAlimeterData(ali)                       # mqtt is used
    else:
        coapPublishAlimeter(ali)                                   # coapp is used
    return "Alimeter started"


@app.route('/stop_ali')                                            # Rote to stop Alimeter
def stop_ali():
    ali.stop()                                                     # alimeter is stopped
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Alimeter is asked to stop!")
    log_file.close() 
    return "Alimeter stopped"


@app.route('/start_weight')                                         # route to start weight sensor    
def start_weight():
    wei.start()                                                     # weightsensor is started
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Weight Sensor is asked to start!")
    log_file.close() 
    if choice == 1:
        PublishData.publishWeightSensorData(wei)                    # mqtt is used
    else:
        coapPublishWeight(wei)                                      # coapp is used
    return "Weight sensor started"


@app.route('/stop_weight')
def stop_weight():
    wei.stop()
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Weight Sensor is asked to stop!")
    log_file.close() 
    return "Weight sensor stopped"


@app.route('/start_pulse')                                              # route to start pulse sensor
def start_pulse():
    pulse.start()                                                       # pulse sensor is tarted
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Pulse Sensor is asked to start!")
    log_file.close() 
    if choice == 1:
        PublishData.publishPulseSensorData(pulse)                       # mqtt is used
    else:
        coapPublishPulse(pulse)                                         # coapp is used
    return "Pulse sensor started"   


@app.route('/stop_pulse')                                               # Route to  stop pulse sensor
def stop_pulse():   
    pulse.stop()                                                        # pulse sensor is stopped
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Pulse Sensor is asked to stop!")
    log_file.close() 
    return "Pulse sensor stopped"

@app.route('/start_device')                                             # Route to start device
def start_device(): 
    device.start()                                                      # start the device
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Device is asked to start!")
    log_file.close() 
    if choice == 1:                                                     # mqtt is used
        PublishData.publishWristHealthBandData(device)
    else:
        coapPublishWristBand(device)                                    # coapp is used
    return "Device started"                                             # Device Started


@app.route('/stop_device')                      # Route to stop device
def stop_device():                              
    device.stop()                               # Device is stopped
    log_file = open('RuntimeLogs/runtime.txt', 'a+')
    logger.log(log_file, "Device is asked to stop!")
    log_file.close() 
    return "Device stopped"


if __name__ == '__main__':
    app.run()                                   # Flask app is started