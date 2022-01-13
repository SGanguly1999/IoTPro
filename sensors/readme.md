## Sensors
    Four sensors are mainly used in this project. As, we are using data from virtual sesor we  have implemeted here four sesors according to their characteristic function using python.

### Sesor Abstraction
    It is the base class for all the sensors. As all the sesors will be used in a single project, we try to keep the basic functionalities same for all the sensors.
    * Parameters:
        * createThread : Reference of the thread which will be used to execute the program
        * time: Current system time
        * executionFlag: Determines the program is executing or not
        * sampleFreq: 
        * setTolerance: 
        * out: 
        * name: Assigned name to the sensor
    * Methods:
        * start: Crete a new thread for every sesnosr and sesor is started.
        * stop: Sensor is stopped and
        * sample_freq: 
        * continuous_generation: random data is genrated after a particular interval of time.
        * characteristicFunc: It is an abstract function as it's different for every sensors.
        * output: Output is  genrated by this function.
        * set_name: sensor_name can be  set using this function.

     