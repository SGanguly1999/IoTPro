from sensors.SensorAbstraction import SensorAbstraction
# WeightSensor inherits SensorAbstraction
class WeightSensor(SensorAbstraction):
   # Constructor
   def __init__(self,sampleFreq):
      SensorAbstraction.__init__(self)     # Calls constructor of parent class
      self.setName("WeightSensor")        # Assign name as Weight Sensor
      self.sample_freq(sampleFreq)         # Assign frequency of the sensor

   # Charcteristics Function
   def characteristicFunc(self,input): 
      h = input + input ** 2                                               # x = x + x ^ 2
      log_file = open(self.file_object, 'a+')                # log_file is opened for logging information
      self.logger.log(log_file, "{} generates {}.".format(self.name, h))   # message is logged
      log_file.close()                                                     # log file is closed
      return h