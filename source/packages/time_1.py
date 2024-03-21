# create a two prints, but 2ns print with delay of 2 secs

# time.sleep : sleeps the code for respective seconds
# syntax : time.sleep(seconds)
import time

print('Hello')
time.sleep(2) # delay for 2 seconds
print('hai')

print('1')
time.sleep(5) # delay for 5 seconds
print('2')

print('1')
time.sleep(0.5) # delay for 5 micro seconds
print('2')