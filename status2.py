#typo error in import
import subprocess

for ping in range(1,10):
       address = "192.168.134." + str(ping)
       res = subprocess.call(['ping', '-c', '3', '-W', '5', address])
       if res == 4:
           print ("ping to", address, "OK")
       elif res == 2:
           print ("no response from", address)
       else:
           print ("ping to", address, "failed!")