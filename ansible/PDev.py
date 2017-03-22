#/usr/bin/env python
import os,commands,time

user=raw_input("Enter User Name")
os.system(" adduser "+ user)
os.system(" service ufw disable ")

