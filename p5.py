from threading import *
from time import sleep

producer = int(input("Enter the nu ber of producers want to perform -> "))
consumer = int(input("Enter the nu ber of consumer want to perform -> "))


class producers(Thread):
    try:
        def run(self):
            for pro in range(producer):
                print("Producer", pro + 1)
                sleep(1)
    except:
        print("Executed except block of producers")


class consumers(Thread):
    try:
        def run(self):
            for con in range(consumer):
                print("consumer", con + 1)
                sleep(1)
    except:
        print("Executed except block of consumers")


t1 = producers()
t2 = consumers()

t1.start()
sleep(0.4)
t2.start()

t1.join()
t2.join()
