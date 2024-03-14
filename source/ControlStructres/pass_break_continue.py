# pass : does nothing
# break : breaks the loop
# continue : skips the current itearation


for i in range(5):
    if i == 2:
        pass
    print(i)

for i in range(5):
    if i == 2:
        break # it breaks the loop and wont run after break
    print(i)


for i in range(5):
    if i == 2:
        continue # it skips the 10th iteration, and runs from 11th
    print(i)


# pass

def sample():
    pass

sample()    