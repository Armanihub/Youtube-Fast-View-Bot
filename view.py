import webbrowser

import time

import os

inpt = input("Enter youtube url: ")

inpt2 = float(input("Enter refresh rate(seconds): "))

inp4 = int(input("Enter views: "))

print("Working...")

print ('<<<<<<<<<<<<<<<<<<<<<<<<<THE VIEW BOT>>>>>>>>>>>>>>>>>>>>>>>>>>')
print ('--------------------------------------------------------------')
print ('||||||||||||||||||||||||||BY Rae Armani||||||||||||||||||||||||||||')
print ('--------------------------------------------------------------')
print ('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

counter =0
while (counter != inp4):
	webbrowser.open(inpt)
	time.sleep(inpt2)
	counter = counter +1
	
