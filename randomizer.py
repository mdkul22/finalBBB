from logger.models import *
import random
import time


def datahandler(data):
    res = eval(data)
    del res[0]
    res.append(random.randint(0, 100))
    return res

if __name__ == "__main__":

    while(1):
        d = BMSData.objects.get(pk=1)
        d.btq1 = datahandler(d.btq1)
        d.btq2 = datahandler(d.btq2)
        d.btq3 = datahandler(d.btq3)
        d.btq4 = datahandler(d.btq4)
        d.save()
        time.sleep(2)
