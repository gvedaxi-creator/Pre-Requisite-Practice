# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:31:52 2026

@author: vedax
"""

class GPS:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = "Home"

    def visit(self, place):
        self.back_stack.append(self.current)
        self.current = place
        self.forward_stack.clear()
        print("Current:", self.current)

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            print("Current:", self.current)
        else:
            print("No previous place")

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            print("Current:", self.current)
        else:
            print("No forward place")


g = GPS()
print(g.current)
g.visit("Nehrunagar")
g.visit("Navaranpura")
g.visit("Memnagar")

g.back()
g.back()
g.forward()
print(g.current)