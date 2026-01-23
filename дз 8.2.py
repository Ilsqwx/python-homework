import time

minuts = int(input("Enter minutes: "))
secounds = minuts * 60

start = time.time()
while time.time() - start < secounds:
    time.sleep(0.1)

print("Time is over!")