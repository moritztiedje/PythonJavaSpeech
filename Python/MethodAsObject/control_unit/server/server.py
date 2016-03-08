from Examples.MethodAsObject.control_unit.server.Components import ConnectionSupervisor


class Server(object):
    def __init__(self, stop_device, connection_timeout):
        ConnectionSupervisor(stop_device, connection_timeout)
