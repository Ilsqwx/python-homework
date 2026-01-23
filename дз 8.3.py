import time

start = time.time()

for i in range(3):
    input("Press Enter for lap ")
    lap = time.time() - start
    print("Lap", i + 1, ":", lap)

print("Total time:", time.time() - start)
