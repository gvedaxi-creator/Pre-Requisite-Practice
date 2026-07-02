# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:32:04 2026

@author: vedax
"""

from collections import deque

class SmartPrinter:
    def __init__(self,max_size=5):
        self.urgent=deque(maxlen=max_size)
        self.normal=deque(maxlen=max_size)
        self.max_size=max_size
    def add_job(self,job,priority='normal'):
        if priority=='urgent':
            if len(self.urgent) >=self.max_size:
                print("[Rejected]Your queue is full.")
                return
            self.urgent.append(job)
        else:
            if len(self.normal) >=self.max_size:
                print("[Rejected]Your queue is full.")
                return
            self.normal.append(job)
    def printing(self):
        if self.urgent:
            job = self.urgent.popleft()
            print(job)
        elif self.normal:
            job = self.normal.popleft()
            print(job)
        else:
            print("Queue is empty")
s = SmartPrinter()

s.add_job("Aadhar card")
s.add_job("DS.pdf")
s.add_job("Marksheet.pdf","urgent")
s.add_job("Invoice")
s.printing()
s.printing()
s.printing()

            