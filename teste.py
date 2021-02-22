line1 =['one','two','three']
line2=['a','b','c']
line3=['mike','jack','ram']

all_data = [line1] + [line2] + [line3]

print(all_data)

from random import random
count = int(random() * 10) + 1

for data in all_data:
    name = 'data/file' + str(count) + '.txt'
    print(name)
    output = open(name, 'w')
    output.write(','.join(data))
    count += 1
    output.close()