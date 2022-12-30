import webbrowser
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread, Barrier
import os

def load_proxies(PATH): # for loading the proxies
    return open(PATH).read().split('\n') 

def load_session(url,proxy): # manage each session
    proxy,port = proxy.split(':')
    profile = webdriver.Chrome()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy)
    profile.set_preference("network.proxy.http_port", port)
    profile.set_preference("network.proxy.ssl", proxy)
    profile.set_preference("network.proxy.ssl_port", port)
    profile.update_preferences()

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
