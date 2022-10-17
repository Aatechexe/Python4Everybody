import re
from tkinter import X
from turtle import xcor
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)