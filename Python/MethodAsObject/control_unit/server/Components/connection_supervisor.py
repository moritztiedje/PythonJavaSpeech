from Support import reactor


class ConnectionSupervisor(object):
    def __init__(self, stop_device, connection_timeout):
        self.__timeout = connection_timeout
        self.__stop_device = stop_device
        self.__timeout_call = None

    def start(self):
        self.__timeout_call = self.__new_timeout_thread()

    def reset_timer(self):
        self.__timeout_call.cancel()
        self.__timeout_call = self.__new_timeout_thread()

    def __new_timeout_thread(self):
        return reactor.call_later(self.__timeout, self.__stop_device)