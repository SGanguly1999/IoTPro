import random                                           # for generating random number
from datetime import datetime                           # datetime to access system time
from datetime import timedelta                          # for date manupulation and differnce of time
import time as timing                                   # 
import threading                                        # for multithreading
from application_logging.logger import App_Logger       # for logging

class SensorAbstraction:
    # Constructor
    def __init__(self):
        self.createThread = None                # Initially no thread is assigned
        self.time = datetime.today()            # current system time
        self.executionFlag = False              # Intially denoting that sesor isn't working
        self.sampleFreq = 1                     # Default sampling rate is 1
        self.setTolerance = None                # Intially there is no error rate assigned
        self.out = -1                           # Initially output  is 1
        self.name = "Sensor"                    # Intially sensor name is Sensor
        self.logger = App_Logger()              # An instanve of logger is created for logging

    # Start the Sensor
    def start(self):
        if self.createThread is None:                           # Starting the sensor by creating thread
            self.executionFlag  = True                          # Denotes that sensor is working
            self.createThread = threading.Thread(target=self.continuous_generation) # New thread is created
            self.createThread.start()                           # thread execution has started
            log_file = open(self.file_object, 'a+')             # log_file is opened for logging information
            self.logger.log(log_file, "{} is started.".format(self.name))   #message is logged
            log_file.close()                                    # log file is closed
        else:
            log_file = open(self.file_object, 'a+')             # log_file is opened for logging information
            self.logger.log(log_file, "{} is already executing.".format(self.name)) # message is logged
            log_file.close()                                    # log file is closed

    def stop(self):
        if self.createThread is not None:           # Stopping the sensor thread by turning executionFlag false
            self.executionFlag=False                # Denotes sensor is stopped
            # join() is used for a particular thread the main thread 
            # will stop executing until the execution of joined thread is complete 
            self.createThread.join()                
            self.out = None                         # No output is  generated
            self.createThread = None                # thread is killed
            log_file = open(self.file_object, 'a+') # log_file is opened for logging information
            self.logger.log(log_file, "{} is stopped.".format(self.name)) # message is logged
            log_file.close()                        # log file is closed
        else:
            log_file = open(self.file_object, 'a+') # log_file is opened for logging information
            self.logger.log(log_file, "{} is not executing.".format(self.name)) # message is logged
            log_file.close()                        # log file is closed

    def sample_freq(self, freq = 1):    # By default, sample frequency by default is set to 1
        self.sampleFreq = freq          # frequency of the sensor is set by freq
        log_file = open(self.file_object, 'a+')                # log_file is opened for logging information
        self.logger.log(log_file, "{} frequency is set to {}.".format(self.name, self.sampleFreq))
        # message is logged
        log_file.close()                # log_file is closed     

    def continuous_generation(self):                        # data is generated continuously
        delta=timedelta(seconds = 1)                        # time difference is set to 1
        while self.executionFlag is not False:              # checking sensor is on/off
                timing.sleep(1 // self.sampleFreq)          # set sleep time of the thread
                input=random.randint(0,100)                 # generate random data
                # random data is passed as parameter to characteristic function
                self.out=self.characteristicFunc(input)
                self.time+=delta                            # time is modified
    def characteristicFunc(self,input):                     # abstract function
        pass

    def tolerance(self,tol = 0):                            # By  default error is set to zero
        self.setTolerance = tol                             # tol is assigned to tolerance

    def output(self):                                       # Output is genrated by this function
        if self.out!=None:                                  # if output is not None
         return self.out                                    # out is returned
        else:
         return None                                        #  nothing is returned

    def setName(self, name = "Sensor"):                     # Intial sensor name is 'Sensor'
        self.name = name                                    # Assign name to the sensor
        self.file_object = 'SensorLogs/'+self.name+'.txt'   # logger_file for the sensor is created
