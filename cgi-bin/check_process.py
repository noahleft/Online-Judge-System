#!/usr/bin/python

import os
pids=[pid for pid in os.listdir('/proc') if pid.isdigit()]
from sys import argv

current_list=[]

for pid in pids:
  try:
    cmd=open(os.path.join('/proc', pid, 'cmdline'), 'r').readline()
    if argv[1] in cmd and not 'python' in cmd:
      current_list.append(pid)
  except IOError:
    continue

print current_list

import signal
for pid in current_list:
  print open(os.path.join('/proc', pid, 'cmdline'), 'r').read()
 # os.kill(int(pid), signal.SIGQUIT)


