#

# create a file 'input.txt'
#     insert the data : 10,20
#
#
# reads the inputs from 'input.txt' using open()/ with
#
# w.a.p to add x,y and put/write the output into 'output.txt'


# steps ....

# step 1 : create input.txt using manually
# step 2: write the data 10,20 manually/ write fn's
# step3: read the data from input.txt
# step4 : split the data with split()

            # data = '10,20'
            #
            # x,y = data.split(',')
            #
            # print(x,y)

# step 5: perform addition operation
# step 6 : create output.txt file and write the data into output.txt


#reads the dara from file

f1 = open('input.txt','r')
data = f1.read()
f1.close()
print(data)

data = data.split(',')
print(data)

x,y = data

print(x,type(x))
print(y,type(y))

z= int(x) + int(y)
print((z))


# wite the data into output.txt

f2 = open('output.txt','w')

msg = f'sum of x+y = {z}'
f2.write(msg)
f2.close()


with open('output2.txt','w') as f3:
    msg = f'sum of x+y = {z}'
    f3.write(msg)
