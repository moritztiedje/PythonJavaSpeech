from Examples.MethodAsObject.control_unit.server import Server


class Device(object):
    CONNECTION_TIMEOUT = 5

    def __init__(self):
        self.server = Server(self.stop, self.CONNECTION_TIMEOUT)

    def stop(self):
        # Stop Everything
        pass
