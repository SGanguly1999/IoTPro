from sensors.SensorAbstraction import SensorAbstraction
# Alimeter inherits SensorAbstraction
class Alimeter(SensorAbstraction):
   # Constructor
   def __init__(self,sampleFreq):
      SensorAbstraction.__init__(self) # Calls constructor of parent class
      self.setName("Alimeter")         # Assign name as Alimeter
      self.sample_freq(sampleFreq)     # Assign frequency of the sensor

   # Characteristics Function
   def characteristicFunc(self,input):
      h = input + input ** 2                                               # x = x + x ^ 2
      log_file = open(self.file_object, 'a+')                # log_file is opened for logging information
      self.logger.log(log_file, "{} generates {}.".format(self.name, h))   # message is logged
      log_file.close()                                                     # log file is closed
      return h
