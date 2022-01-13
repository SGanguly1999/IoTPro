# The library is useful to fetch the date and time of system
from datetime import datetime
# The class is used to log the information during reuntime
class App_Logger:
    # Constructor
    def __init__(self):
        pass
    # The  method is used to log the message
    def log(self, file_object, log_message):
        self.now = datetime.now()           # Get system time
        self.date = self.now.date()         # Get system date
        self.current_time = self.now.strftime("%H:%M:%S")   # Create current time and date as string
        file_object.write(str(self.date)+"/"+str(self.current_time)+"\t\t"+log_message+"\n")    # Log message with current time and date