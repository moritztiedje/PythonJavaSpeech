from MethodAsObject.control_unit.server.Components.ConnectionSupervisor import ConnectionSupervisor


class Server(object):
    def __init__(self, stop_device, connection_timeout):
        ConnectionSupervisor(stop_device, connection_timeout)
