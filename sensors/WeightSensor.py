from sensors.SensorAbstraction import SensorAbstraction
class WeightSensor(SensorAbstraction):

   def __init__(self,sampleFreq):
       SensorAbstraction.__init__(self)
       self.sample_freq(sampleFreq)
       self.setName("Weight Sensor")

   def characteristicFunc(self,input):
       h = input + input ** 2
       return h