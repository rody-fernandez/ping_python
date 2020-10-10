import subprocess
import os
with open(os.devnull, "wb") as limbo:
           for n in range(1, 10):
                   ip="192.168.134.{0}".format(n)
                   result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                           stdout=limbo, stderr=limbo).wait()
                   if result == 4 :
                           print (ip, "active")
                   elif result == 2:
                           print (ip, "inactive")
                   else:
                           print (ip, "failed")