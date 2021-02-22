line1 =['one','two','three']
line2=['a','b','c']
line3=['mike','jack','ram']

all_data = [line1] + [line2] + [line3]

count = 3

for data in all_data:
    output = open('data/file' + str(count) + '.txt', 'w')
    output.write(','.join(data))
    count += 1
    output.close()