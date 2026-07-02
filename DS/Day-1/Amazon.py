# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:58:16 2026

@author: vedax
"""

class ConveyorBelt:
    def __init__(self):
        self.slots = [None] * 8

    def add(self, index, product):
        self.slots[index] = product

    def check(self, index):
        print("Product:", self.slots[index])

    def find(self, product):
        if product in self.slots:
            print("Found at slot", self.slots.index(product))
        else:
            print("Product not found")

    def update(self, index, product):
        self.slots[index] = product

    def is_full(self):
        if None not in self.slots:
            print("Conveyor Belt is Full")
        else:
            print("Space Available")


belt = ConveyorBelt()

belt.add(0, "Lipstick")
belt.add(1, "Concealer")
belt.add(2, "Compact")

belt.check(1)
belt.update(2, "Perfume")
belt.check(2)
belt.is_full()
belt.find("Nail Paint")