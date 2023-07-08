fname = input('Enter file name: ')
try:
    filehandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in filehandle:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
for key in counts:
        print(key, counts[key])
sorted_counts = sorted(counts.items(), key=lambda x: x[0])
for key, value in sorted_counts:
    print(key, value)

