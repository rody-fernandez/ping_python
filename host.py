#!/usr/local/bin/python

import subprocess, time

hosts = ('192.168.134.5', '192.168.133.33', '192.168.133.37')

def ping(host):
  ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
    stdout=open('/dev/null', 'w'),
    stderr=open('/dev/null', 'w'))
  return ret == 0

def net_is_up():
  print ("[%s] Checking if network is up..." % time.strftime("%Y-%m-%d %H:%M:%S"))

  xstatus = 1

  for h in hosts:
    if ping(h):
      print ("[%s] Network is up!" % time.strftime("%Y-%m-%d %H:%M:%S"))
      xstatus = 0
      break

  if xstatus:
    print ("[%s] Network is down :(" % time.strftime("%Y-%m-%d %H:%M:%S"))

  return xstatus

quit(net_is_up())