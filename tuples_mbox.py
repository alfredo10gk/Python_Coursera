# top 10 most common words
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print('File cannot be opened:', name)
    exit()
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for key, val in counts.items():
    newtupl = (val, key)
    lst.append(newtupl)
lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
    print(key, val)
    
