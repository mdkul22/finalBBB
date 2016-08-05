import csv
import itertools
from randval import randgen
# import serial

# ser = serial.Serial(port='dev/ttyACM0', baudrate=9600, timeout=1)


class Logger():

    """this class works as a data handler """

    def __init__(self):
        self.sensor_val = {
            'btq1': [], 'btq2': [], 'btq3': [], 'btq4': [], 'mtl': [], 'mtr': [], 'mct': [],
            'mc2mrc': [], 'mc2mlc': [], 'mc2bc': [],
            'soc': [], 'maxdiscC': [], 'maxc': [], 'mindiscC': [],
            'speedfl': [], 'speedfr': [], 'speedbr': [], 'speedbl': []
        }
        self.sensor_names = self.sensor_val.keys()

    def readr(self):
        # x = ser.read()
        x = randgen()

        if x == '':
            return 'x'

        else:
            return x

    def checkr(self, value):
        if value[0] == 'a':
            self.sensor_val['btq1'].append(value[1:])

        elif value[0] == 'b':
            self.sensor_val['btq2'].append(value[1:])

        elif value[0] == 'c':
            self.sensor_val['btq3'].append(value[1:])

        elif value[0] == 'd':
            self.sensor_val['btq4'].append(value[1:])

        elif value[0] == 'e':
            self.sensor_val['mtl'].append(value[1:])

        elif value[0] == 'f':
            self.sensor_val['mtr'].append(value[1:])

        elif value[0] == 'g':
            self.sensor_val['mct'].append(value[1:])

        elif value[0] == 'h':
            self.sensor_val['mc2mrc'].append(value[1:])

        elif value[0] == 'i':
            self.sensor_val['mc2mlc'].append(value[1:])

        elif value[0] == 'j':
            self.sensor_val['mc2bc'].append(value[1:])

        elif value[0] == 'k':
            self.sensor_val['soc'].append(value[1:])

        elif value[0] == 'l':
            self.sensor_val['maxdiscC'].append(value[1:])

        elif value[0] == 'm':
            self.sensor_val['maxc'].append(value[1:])

        elif value[0] == 'n':
            self.sensor_val['mindiscC'].append(value[1:])

        elif value[0] == 'o':
            self.sensor_val['speedfl'].append(value[1:])

        elif value[0] == 'p':
            self.sensor_val['speedfr'].append(value[1:])

        elif value[0] == 'q':
            self.sensor_val['speedbr'].append(value[1:])

        else:
            self.sensor_val['speedbl'].append(value[1:])

    def save_list_in_csv(self):

        d = self.sensor_val
        with open("fatdata.csv", "wb") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(d.keys())
            writer.writerows(itertools.izip_longest(*d.values()))

if __name__ == "__main__":
    x = Logger()
    for y in range(0, 90):
        x.checkr(x.readr())
    for key, val in x.sensor_val.items():
        print key, "=>", val
    x.save_list_in_csv()
