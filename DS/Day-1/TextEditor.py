# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:44:45 2026

@author: vedax
"""

class TextEditor:
    def __init__(self):
        self.l=[]
    def type(self,char):
        self.l.append(char)
    def undo(self):
        self.l.pop()
    def getText(self):
        s="".join(self.l)
        print(s)

t=TextEditor()

t.type('A')
t.type('B')
t.type('C')
t.getText()
t.undo()
t.type('D')
t.getText()