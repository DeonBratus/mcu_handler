from rclpy.node import Node
from colorama import Fore, Style
import rclpy
import time

from mcu_solver.mcu_handler import SerialMCU
from robot_interface.msg import McuData

class ReceiverMCU(Node):
    def __init__(self):
        super().__init__('ReceiverNode')
        self.mcu_publisher = self.create_publisher(McuData, 'EconstBot/DataMcu', 10)
        self.timer = self.create_timer(0.4 , self.send_msg)

        self.mcu = SerialMCU()
        self.mcu.device.port = "/dev/ttyUSB0"
        self.mcu.device.baudrate = 9600

        try:
            self.mcu.connect_device()

        except Exception as err:
            print(Fore.YELLOW, end='')
            print('Device is not connected, try again and check your port')
            print(Style.RESET_ALL, end='')

    def send_msg(self):
        try:
            interface_mcu = McuData()
            mcu_data = self.mcu.listen_device()
            
            interface_mcu.mcu_str_data = mcu_data
            self.mcu_publisher.publish(interface_mcu) 
        except Exception as err:
            time.sleep(1)


def main(args=None):
    rclpy.init(args=args)
    rec_mcu = ReceiverMCU()
    rclpy.spin(rec_mcu)
    rec_mcu.destroy_node()
    rclpy.shutdown()
    
if __name__ == 'main':
    main()