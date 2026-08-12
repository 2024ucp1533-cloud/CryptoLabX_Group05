import subprocess
import hashlib

username = "admin"
password = "admin123"

cmd = input("Enter command: ")
subprocess.call(cmd, shell=True)

hash = hashlib.md5(password.encode())
print(hash.hexdigest())
