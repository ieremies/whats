#!/usr/bin/env python3

import server
import client
from _thread import *
from time import sleep

# Start the receiver server
start_new_thread(server.receiver, ())

sleep(1)
ip_address = input("IP do coleguinha: ")
client.sender(ip_address)
