import random
from datetime import datetime,timedelta
import time as timing
import threading
from application_logging.logger import App_Logger

class SensorAbstraction:
    def __init__(self):
        self.createThread = None
        self.time = datetime.today()
        self.executionFlag = False
        self.sampleFreq = 1
        self.setTolerance = None
        self.out = -1
        self.name = "Sensor"
        self.logger = App_Logger()

    def start(self):
        if self.createThread is None:  # Starting the sensor by creating thread
            self.executionFlag  = True
            self.createThread = threading.Thread(target=self.continuous_generation)
            self.createThread.start()
            log_file = open(self.file_object, 'a+')
            self.logger.log(log_file, "{} is started.".format(self.name))
            log_file.close()
        else:
            log_file = open(self.file_object, 'a+')
            self.logger.log(log_file, "{} is already executing.".format(self.name))
            log_file.close()

    def stop(self):
        if self.createThread is not None:  # Stopping the sensor thread by turning executionFlag false
            self.executionFlag=False
            self.createThread.join()
            self.out = None
            self.createThread = None
            log_file = open(self.file_object, 'a+')
            self.logger.log(log_file, "{} is stopped.".format(self.name))
            log_file.close()
        else:
            log_file = open(self.file_object, 'a+')
            self.logger.log(log_file, "{} is not executing.".format(self.name))
            log_file.close()

    def sample_freq(self, freq = 1):  # Sample frequency by default is set to 1
        self.sampleFreq = freq

    def continuous_generation(self):
        delta=timedelta(seconds = 1)
        while self.executionFlag is not False:
                timing.sleep(1 // self.sampleFreq)
                input=random.randint(0,100)
                self.out=self.characteristicFunc(input)
                self.time+=delta
    def characteristicFunc(self,input):
        pass

    def tolerance(self,tol = 0):
        self.setTolerance = tol

    def output(self):
        if self.out!=None:
         return self.out
        else:
         return None

    def setName(self, name = "Sensor"):
        self.name = name
        self.file_object = 'SensorLogs/'+self.name+'.txt'
