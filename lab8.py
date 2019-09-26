from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
from datetime import datetime

host = None
uname = None
pw = None

if host == None:
    host = input("Hostname or IP: ")
if uname == None:
    uname = input("Username: ")
if pw == None:
    pw = getpass("Password: ")

dev = Device(host=host, user=uname, password=pw)
dev.open()
cu = Config(dev)
diff = cu.diff()
print(cu.commit_check())
fd = open("rollbacks.txt", "a")
mess = "Uncommited config found. Rollback"
roll = "Rollback done"
noroll = "The latetst config present. No rollback needed"
date = str(datetime.now())
if diff:
    print(mess)
    fd.write(date + " " + mess)
    cu.rollback()
    print(roll)
    fd.write(date + " " + roll)
else:
    print(noroll)
    fd.write(date + " " + noroll)
dev.close()
df.close()
