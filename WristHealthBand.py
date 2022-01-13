from datetime import timedelta, datetime
from sensors.Accelorometer import Accelerometer
from sensors.PulseSensor import PulseSensor
from sensors.WeightSensor import WeightSensor
from sensors.Alimeter import Alimeter
import threading


class WristHealthBand:
    def __init__(self, sampleFreq=1):
        self.sampleFreq = sampleFreq
        self.acc = Accelerometer(sampleFreq=sampleFreq)
        self.pulse = PulseSensor(sampleFreq=sampleFreq)
        self.alti = Alimeter(sampleFreq=sampleFreq)
        self.weight = WeightSensor(sampleFreq=sampleFreq)
        self.createThread = None
        self.out = -1
        self.name = "Pz Wrist Health Band"
        self.grav_acc = 9.8
        self.ini_height = 0
        self.executionFlag = False

    def start(self):
        if self.createThread is None:
            self.acc.start()
            self.pulse.start()
            self.alti.start()
            self.weight.start()
            self.executionFlag = True
            self.createThread = threading.Thread(target=self.__circuitDesign)
            self.createThread.start()
            print(self.name + " is started")

    def stop(self):
        if self.createThread is not  None:  # Stopping the sensor thread by turning executionFlag false
            self.executionFlag = False
            self.createThread.join()
            self.out = None
            self.createThread = None
            self.acc.stop()
            self.pulse.stop()
            self.alti.stop()
            self.weight.stop()
            print(self.name + " is stopped")
        else:
            print(self.name + " is not executing")

    def __circuitDesign(self):
        while self.executionFlag is not False:
            height = self.alti.output()
            self.out += (self.acc.output() + self.grav_acc) * self.weight.output() * (height - self.ini_height)
            self.ini_height = height

    def setName(self, name="Sensor"):
        self.name = name

    def output(self):
        if self.out != None:
            return (str(datetime.today()) + " " + self.name + "---calories burnt is " + str(
                self.out) + " and pulse rate is " + str(self.pulse.output()))
        else:
            return None
