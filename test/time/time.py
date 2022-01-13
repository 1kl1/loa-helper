from screeenshot import saveScreenShot
import sys
from os import path
import time as t

print(path.abspath(__file__))
start = t.time()
for i in range(0, 1):
    saveScreenShot(1250, 65, 50, 20, "tmp/test.bmp")
end = t.time()

print(end-start)
