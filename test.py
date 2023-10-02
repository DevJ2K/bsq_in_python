import os
import time

for i in range(10):
    print(f"Compteur {i}\n22{i} avec \\r: {i}", end='\r')
    time.sleep(1)