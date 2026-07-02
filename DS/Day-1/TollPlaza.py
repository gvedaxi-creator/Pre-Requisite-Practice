# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:00:22 2026

@author: vedax
"""

from collections import deque

class TollPlaza:
    def __init__(self):
        self.queue = deque(maxlen=5)

    def enter(self, vehicle):
        if len(self.queue) == 5:
            print("Toll Plaza Full")
        else:
            self.queue.append(vehicle)
            print(vehicle, "entered")

    def exit(self):
        if len(self.queue) == 0:
            print("No vehicle")
        else:
            print(self.queue.popleft(), "left")

    def display(self):
        print(list(self.queue))


t = TollPlaza()

t.enter("Truck")
t.enter("Bus")
t.enter("Car")
t.display()
t.enter("Bike")
t.enter("Minivan")
t.exit()
t.display()
t.enter("Activa")
t.display()
t.enter("Activa")