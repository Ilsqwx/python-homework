import time

start = time.time()

for i in range(1_000_000):
    pass

end = time.time()

print("Время выполнения цикла:", end - start)