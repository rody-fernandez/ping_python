import pyping

r = pyping.ping('192.168.0.1')
print(r.ret_code)