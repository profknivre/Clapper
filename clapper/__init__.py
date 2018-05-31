__version__ = '0.1.2'
# ICStation ICSE014A relay board handler


import serial
from time import sleep


class Clapper:
    def __init__(self):
        self.ser = serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0',
                                 9600, timeout=0.1)

        self.ser.write(b'PQPQPQPQPQPQ')
        _ = self.ser.read(10)
        self.ser.write(b'Q')
        sleep(.1)
        self.ser.write(b'\xff')
        self.value = 0xff

    def set(self, what):
        """
        set output state to 'what'
        :param what: int >=0 <=255
        :return:
        """
        if what < 0 or what > 255:
            raise Exception('Clapper::set Value out of range {:d}'.format(what))

        self.value = what
        self.ser.read_all()
        # sleep(.1)
        self.ser.write(bytes([self.value, ]))
        # print(bytes([self.value, ]))
        # sleep(.1)
        print('setting: {:08b}'.format(self.value))

        return self.value

    def off(self, which):
        """
        disable output no 'which'

        reversed logic
        :param which: int
        :return:
        """
        if which < 0 or which > 7:
            raise Exception('Clapper Value out of range {:d}'.format(which))

        val = self.value | 1 << which
        return self.set(val)

    def on(self, which):
        """
        enable output no 'which'

        reversed logic
        :param which: int
        :return:
        """
        if which < 0 or which > 7:
            raise Exception('Clapper Value out of range {:d}'.format(which))

        val = self.value & ~(1 << which)
        return self.set(val)

    def all_on(self):
        """
        enable all outputs
        :return:
        """
        return self.set(0)

    def all_off(self):
        """
        disable all outputs
        :return:
        """
        return self.set(0xff)

    def is_on(self, which):
        if which < 0 or which > 7:
            raise Exception('Clapper Value out of range {:d}'.format(which))

        bit = (1 << which)
        return self.value & bit == 0

    def toggle(self, which):
        if which < 0 or which > 7:
            raise Exception('Clapper Value out of range {:d}'.format(which))

        return self.is_on(which) and self.off(which) or self.on(which)

    # def _dispatch(self, method, params):
    #     pass
