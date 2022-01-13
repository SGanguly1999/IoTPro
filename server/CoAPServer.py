import aiocoap.resource as resource
import aiocoap
import threading
import logging
import asyncio


class AccelerometerResource(resource.ObservableResource):
    """This resource supports the GET and PUT methods and is observable.
    GET: Return current state of the sensor
    PUT: Update state of alarm and notify registered observers"""

    def __init__(self):
        super().__init__()

        self.status = None
        self.has_observers = False
        self.notify_observers = False

    # Ensure observers are notify if required
    def notify_observers_check(self):
        while True:
            if self.has_observers and self.notify_observers:
                print('Notifying observers')
                self.updated_state()
                self.notify_observers = False

    # Observers change event callback
    def update_observation_count(self, count):
        if count:
            self.has_observers = True
        else:
            self.has_observers = False

    # Handles GET request or observer notify
    async def render_get(self, request):
        print('Return accelerometer state: %s' % self.status)
        payload = b'%s' % self.status.encode('ascii')

        return aiocoap.Message(payload=payload)

    # Handles PUT request
    async def render_put(self, request):
        self.status = request.payload.decode('ascii')
        print('Update accelerometer state: %s' % self.status)
        self.notify_observers = True

        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'%s' % self.status.encode('ascii'))

class AlimeterResource(resource.ObservableResource):
    """This resource supports the GET and PUT methods and is observable.
    GET: Return current state of alarm
    PUT: Update state of alarm and notify registered observers"""

    def __init__(self):
        super().__init__()

        self.status = "OFF"
        self.has_observers = False
        self.notify_observers = False

    # Ensure observers are notify if required
    def notify_observers_check(self):
        while True:
            if self.has_observers and self.notify_observers:
                print('Notifying observers')
                self.updated_state()
                self.notify_observers = False

    # Observers change event callback
    def update_observation_count(self, count):
        if count:
            self.has_observers = True
        else:
            self.has_observers = False

    # Handles GET request or observer notify
    async def render_get(self, request):
        print('Return alimeter state: %s' % self.status)
        payload = b'%s' % self.status.encode('ascii')

        return aiocoap.Message(payload=payload)

    # Handles PUT request
    async def render_put(self, request):
        self.status = request.payload.decode('ascii')
        print('Update alimeter state: %s' % self.status)
        self.notify_observers = True

        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'%s' % self.status.encode('ascii'))

class PulseSensorResource(resource.ObservableResource):
    """This resource supports the GET and PUT methods and is observable.
    GET: Return current state of alarm
    PUT: Update state of alarm and notify registered observers"""

    def __init__(self):
        super().__init__()

        self.status = "OFF"
        self.has_observers = False
        self.notify_observers = False

    # Ensure observers are notify if required
    def notify_observers_check(self):
        while True:
            if self.has_observers and self.notify_observers:
                print('Notifying observers')
                self.updated_state()
                self.notify_observers = False

    # Observers change event callback
    def update_observation_count(self, count):
        if count:
            self.has_observers = True
        else:
            self.has_observers = False

    # Handles GET request or observer notify
    async def render_get(self, request):
        print('Return pulse sensor state: %s' % self.status)
        payload = b'%s' % self.status.encode('ascii')

        return aiocoap.Message(payload=payload)

    # Handles PUT request
    async def render_put(self, request):
        self.status = request.payload.decode('ascii')
        print('Update pulse sensor state: %s' % self.status)
        self.notify_observers = True

        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'%s' % self.status.encode('ascii'))

class WeightSensorResource(resource.ObservableResource):
    """This resource supports the GET and PUT methods and is observable.
    GET: Return current state of alarm
    PUT: Update state of alarm and notify registered observers"""

    def __init__(self):
        super().__init__()

        self.status = "OFF"
        self.has_observers = False
        self.notify_observers = False

    # Ensure observers are notify if required
    def notify_observers_check(self):
        while True:
            if self.has_observers and self.notify_observers:
                print('Notifying observers')
                self.updated_state()
                self.notify_observers = False

    # Observers change event callback
    def update_observation_count(self, count):
        if count:
            self.has_observers = True
        else:
            self.has_observers = False

    # Handles GET request or observer notify
    async def render_get(self, request):
        print('Return weight sensor state: %s' % self.status)
        payload = b'%s' % self.status.encode('ascii')

        return aiocoap.Message(payload=payload)

    # Handles PUT request
    async def render_put(self, request):
        self.status = request.payload.decode('ascii')
        print('Update weight sensor state: %s' % self.status)
        self.notify_observers = True

        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'%s' % self.status.encode('ascii'))
class WristHealthBandResource(resource.ObservableResource):
    """This resource supports the GET and PUT methods and is observable.
    GET: Return current state of alarm
    PUT: Update state of alarm and notify registered observers"""

    def __init__(self):
        super().__init__()

        self.status = "OFF"
        self.has_observers = False
        self.notify_observers = False

    # Ensure observers are notify if required
    def notify_observers_check(self):
        while True:
            if self.has_observers and self.notify_observers:
                print('Notifying observers')
                self.updated_state()
                self.notify_observers = False

    # Observers change event callback
    def update_observation_count(self, count):
        if count:
            self.has_observers = True
        else:
            self.has_observers = False

    # Handles GET request or observer notify
    async def render_get(self, request):
        print('Return device state: %s' % self.status)
        payload = b'%s' % self.status.encode('ascii')

        return aiocoap.Message(payload=payload)

    # Handles PUT request
    async def render_put(self, request):
        self.status = request.payload.decode('ascii')
        print('Update device state: %s' % self.status)
        self.notify_observers = True

        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'%s' % self.status.encode('ascii'))


logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)


def main():
    # Resource tree creation
    root = resource.Site()
    accResource = AccelerometerResource()
    aliResource = AlimeterResource()
    pulseResource = PulseSensorResource()
    weightResource = WeightSensorResource()
    wristbandResource = WristHealthBandResource()
    root.add_resource(['accelerometer'], accResource)
    root.add_resource(['alimeter'], aliResource)
    root.add_resource(['pulse'], pulseResource)
    root.add_resource(['weight'], weightResource)
    root.add_resource(['wristband'], wristbandResource)
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('localhost', 5683)))

    # Spawn a daemon to notify observers when accelerometer status changes
    observers_notifier_acc = threading.Thread(target=accResource.notify_observers_check)
    observers_notifier_acc.daemon = True
    observers_notifier_acc.start()

    # Spawn a daemon to notify observers when alimeter status changes
    observers_notifier_ali = threading.Thread(target=aliResource.notify_observers_check)
    observers_notifier_ali.daemon = True
    observers_notifier_ali.start()

    # Spawn a daemon to notify observers when pulse sensor  status changes
    observers_notifier_pulse = threading.Thread(target=pulseResource.notify_observers_check)
    observers_notifier_pulse.daemon = True
    observers_notifier_pulse.start()

    # Spawn a daemon to notify observers when weight sensor status changes
    observers_notifier_weight = threading.Thread(target=weightResource.notify_observers_check)
    observers_notifier_weight.daemon = True
    observers_notifier_weight.start()

    # Spawn a daemon to notify observers when wrist band  status changes
    observers_notifier_wristband = threading.Thread(target=wristbandResource.notify_observers_check)
    observers_notifier_wristband.daemon = True
    observers_notifier_wristband.start()

    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()

