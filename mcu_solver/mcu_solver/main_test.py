import serial
class SerialMCU:

    def __init__(self, port = 'COM7', baudrate = 115200 ) -> None:
        self.device = serial.Serial()
        self.device.port = port
        self.device.baudrate = baudrate

    def connect_device(self):
        try:
            self.device.open()
            print(f'Device connected on port {self.device.port}')
        except Exception as err:
            raise ConnectionError('Erorr to connect')

    def listen_device(self):
        serial_data = self.device.readline()
        self.decode_data = serial_data.decode('utf-8')
        return self.decode_data
        
susb = SerialMCU()
susb.baudrate = 115200
susb.connect_device()
while True:
    try:
        print(susb.listen_device())
    except Exception as err:
        pass