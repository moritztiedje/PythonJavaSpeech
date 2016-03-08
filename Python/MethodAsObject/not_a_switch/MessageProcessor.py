class MessageProcessor(object):
    def __init__(self):
        self.message_dict = {'Request Address': self.__handle_request,
                             'Error': self.__show_error,
                             'Pumpkins': self.__eat_pumpkins,
                             'C4': self.__area_is_clear}

    def process(self, message, *parameters):
        message_method = self.message_dict[message]
        message_method(*parameters)

    @staticmethod
    def __handle_request(address, name):
        print("Searching Address: %s, %s" % (name, address))

    @staticmethod
    def __show_error(error_message):
        print("Error: %s" % error_message)

    @staticmethod
    def __eat_pumpkins(*pumpkins):
        for pumpkin in pumpkins:
            print("Yummy, %s" % pumpkin)

    @staticmethod
    def __area_is_clear():
        print('Area clear')

processor = MessageProcessor()
processor.process('Request Address', 'Grove Street', 'Terry James')
processor.process('Error', 'Something')
processor.process('Pumpkins', 'Winter Squash', 'Field Pumpkin', 'Crookneck Pumpkin', 'Cucurbita Agyrosperma')
processor.process('C4')