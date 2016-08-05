from smbus import SMbus
from time import sleep


def rxi2c(address, register):
    while 1:
        bus_1 = SMbus(1)
        x = bus_1.read_byte_data(address, register)
        y = bus_1.read_byte_data(address, register + 1)
        y = y << 8
        y = y + x
        return y
        sleep(0.5)
