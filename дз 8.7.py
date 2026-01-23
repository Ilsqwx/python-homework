import random
import time

print("wellcome to reaction game , in a few seconds u lbe see prepare message, after it a random paus will happen and then a go message appears after go message press enter button asap" )
time.sleep(3)
print("prepare")
time.sleep(random.randint(2,7))
print("go!")
start = time.time()
input()
end = time.time()
print("your reaction time is ", end - start, " seconds")


