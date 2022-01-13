from sensors.SensorAbstraction import SensorAbstraction
class PulseSensor(SensorAbstraction):

   def __init__(self,sampleFreq):
       SensorAbstraction.__init__(self)
       self.sample_freq(sampleFreq)
       self.setName("Pulse sensor")

   def characteristicFunc(self,input):
       h = input + input ** 2
       return h
