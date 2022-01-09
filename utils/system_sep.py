import os

if os.name == "nt":
    seq = "\\"
elif os.name == "unix":
    seq = "/"
else:
    seq = ""