import paho.mqtt.client as paho
import time as timing
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))



client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("SoumyadeepIoT", "SoumyadeepIoT/2021")

# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("8aaf6301429844cfa525110f49856bff.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

def publishAccelerometerData(acc):
 k=1
 while k!=None:
  k=acc.output()
  if(k!=None):
   client.publish("mqtt/Accelerometer", payload=k, qos=1)
   client.loop()
  timing.sleep(1 // acc.sampleFreq)

def publishAlimeterData(ali):
    k=1
    while k!=None:
        k=ali.output()
        if(k!=None):
            client.publish("mqtt/Alimeter",payload=k, qos=1)
            client.loop()
        timing.sleep(1 // ali.sampleFreq)

def publishPulseSensorData(pulse):
    k = 1
    while k != None:
        k = pulse.output()
        if (k != None):
            client.publish("mqtt/PulseSensor", payload=k, qos=1)
            client.loop()
        timing.sleep(1 // pulse.sampleFreq)

def publishWeightSensorData(wei):
    k = 1
    while k != None:
        k = wei.output()
        if (k != None):
            client.publish("mqtt/WeightSensor", payload=k, qos=1)
            client.loop()
        timing.sleep(1 // wei.sampleFreq)

def publishWristHealthBandData(device):
    k = 1
    while k != None:
        k = device.output()
        if (k != None):
            client.publish("mqtt/WristHealthBand", payload=k, qos=1)
            client.loop()
        timing.sleep(1 // device.sampleFreq)