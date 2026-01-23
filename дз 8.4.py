import string
import random
import time

lst = []
for i in range(8):
    lst.append(random.choice(string.ascii_letters + string.digits))
    time.sleep(0.01)
print("here is your password:", "".join(lst))

