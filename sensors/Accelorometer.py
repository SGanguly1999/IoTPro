from sensors.SensorAbstraction import SensorAbstraction
# Accelerometer inherits SensorAbstraction
class Accelerometer(SensorAbstraction):
    # Constructor 
    def __init__(self,sampleFreq):
       SensorAbstraction.__init__(self)
       self.sample_freq(sampleFreq)         # Assign frequency of the sensor
       self.setName("Accelorometer")        # Assign name as Accelorometer
    # Characteristics Function
    def characteristicFunc(self,input):
       h = input + input ** 2               # res = res + res ^ 2
       return h
