## Sensors
    Four sensors are mainly used in this project. As, we are using data from virtual sesor we  have implemeted here four sesors according to their characteristic function using python.

### SesorAbstraction
    It is the base class for all the sensors. As all the sesors will be used in a single project, we try to keep the basic functionalities same for all the sensors.
    * Parameters:
        * createThread : Reference of the thread which will be used to execute the program
        * time: Current system time
        * executionFlag: Determines the sensor is working or not
        * sampleFreq: It is sampling rate which denotes number of times the signal generates data
        * setTolerance: Error rate of sensor
        * out: Output of  the sensor
        * name: Assigned name to the sensor
    * Methods:
        * start: Crete a new thread for every sesnosr and sesor is started
        * stop: Sensor is stopped and the thread which is used to run the sensor is killed
        * sample_freq: It is used to set the frequency of the sensor
        * continuous_generation: random data is genrated after a particular interval of time
        * characteristicFunc: It is an abstract function as it's different for every sensors
        * output: Output is  genrated by this function
        * set_name: sensor_name can be  set using this function

### WeightSensor
    Weight Sensor is implemented in this file. It inherits the class SensorAbstraction.
    * Constructor:
        * SampleFreq is used to set the frequency which is passed in the constructor
        * Sensor name is assigned by "Weight Sensor"
    * characteristicFunc:
        * x^2 + x is used as characteristics function

### Accelorometer
    Accelorometer Sensor is implemented in this file. It inherits the class SensorAbstraction.
    * Constructor:
        * SampleFreq is used to set the frequency which is passed in the constructor
        * Sensor name is assigned by "Accelorometer"
    * characteristicFunc:
        * x^2 + x is used as characteristics function

### PulseSensor
    PulseSensor is implemented in this file. It inherits the class SensorAbstraction.
    * Constructor:
        * SampleFreq is used to set the frequency which is passed in the constructor
        * Sensor name is assigned by "PulseSensor"
    * characteristicFunc:
        * x^2 + x is used as characteristics function

### PulseSensor
    PulseSensor is implemented in this file. It inherits the class SensorAbstraction.
    * Constructor:
        * SampleFreq is used to set the frequency which is passed in the constructor
        * Sensor name is assigned by "PulseSensor"
    * characteristicFunc:
        * x^2 + x is used as characteristics function

### Alimeter
    Alimeter is implemented in this file. It inherits the class SensorAbstraction.
    * Constructor:
        * SampleFreq is used to set the frequency which is passed in the constructor
        * Sensor name is assigned by "Alimeter"
    * characteristicFunc:
        * x^2 + x is used as characteristics function
