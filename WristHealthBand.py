from datetime import datetime                           # for system date and time                   
from sensors.Accelorometer import Accelerometer         # accelorometer is imported
from sensors.PulseSensor import PulseSensor             # pulse sensor is imported
from sensors.WeightSensor import WeightSensor           # weight sensor is imported
from sensors.Alimeter import Alimeter                   # alimeter is imported
import threading                                        # for multithreading
from application_logging.logger import App_Logger       # for logging


class WristHealthBand:
    def __init__(self, sampleFreq=1):
        # frequency is set to each sensor
        self.sampleFreq = sampleFreq
        # instance of sensors are created
        self.acc = Accelerometer(sampleFreq=sampleFreq)
        self.pulse = PulseSensor(sampleFreq=sampleFreq)
        self.alti = Alimeter(sampleFreq=sampleFreq)
        self.weight = WeightSensor(sampleFreq=sampleFreq)
        # Intially no thread is generated
        self.createThread = None
        # Initial output is -1
        self.out = -1
        # Assign name to the device
        self.name = "Pz Wrist Health Band"
        # Gravity is assigned
        self.grav_acc = 9.8
        # Initial height is zero
        self.ini_height = 0
        # Initially it's not executing, so set to false
        self.executionFlag = False
        # for logging
        self.logger = App_Logger()
        # file for logging
        self.file_object = 'RuntimeLogs/runtime.txt'

    def start(self):
        # Device is starting
        if self.createThread is None:
            self.acc.start()                                                            # All the sensors are starting
            self.pulse.start()
            self.alti.start()
            self.weight.start()
            log_file = open(self.file_object, 'a+')
            self.logger.log(log_file, "All the sensors are started.")
            self.executionFlag = True
            self.createThread = threading.Thread(target=self.__circuitDesign)           # A thread is assigned to start the object  
            self.createThread.start()                                                   # Device is started
            self.logger.log(log_file, "{} is started.".format(self.name))
            log_file.close()

    def stop(self):
        if self.createThread is not  None:                                         # Stopping the device thread by turning executionFlag false
            self.executionFlag = False
            self.createThread.join()
            self.out = None
            self.createThread = None                                              # Device thread is deleted                                 
            log_file = open(self.file_object, 'a+')
            self.logger.log(log_file, "{} is stopped.".format(self.name))
            self.acc.stop()
            self.pulse.stop()
            self.alti.stop()
            self.weight.stop()                                                    # All the sensors are stopped
            self.logger.log(log_file, "All the sensors are stopped")
            log_file.close()
        else:
            log_file = open(self.file_object, 'a+')
            self.logger.log(log_file, "{} isn't executing.".format(self.name))
            log_file.close()

    def __circuitDesign(self):
        while self.executionFlag is not False:
            height = self.alti.output()
            self.out += (self.acc.output() + self.grav_acc) * self.weight.output() * (height - self.ini_height)     # BMI is calculated
            log_file = open(self.file_object, 'a+')
            self.logger.log(log_file, "Device Output: ".format(self.out))
            log_file.close()
            self.ini_height = height

    def setName(self, name="Sensor"):
        log_file = open(self.file_object, 'a+')                                     
        self.logger.log(log_file, "Device is assigned by name {}.".format(name))
        log_file.close()
        self.name = name                                                                            # Name is assigned to the device

    def output(self):
        if self.out != None:                                                                        # Output is logged and returned
            log_file = open(self.file_object, 'a+')                                     
            self.logger.log(log_file, "{} {} --- calories burnt is {} and pulse rate is {}.".format(str(datetime.today, str(self.out), str(self.out), str(self.pulse.output()))))
            log_file.close()               
            return (str(datetime.today()) + " " + self.name + "---calories burnt is " + str(self.out) + " and pulse rate is " + str(self.pulse.output()))
        else:
            return None
