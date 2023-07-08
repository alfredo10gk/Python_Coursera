data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1: sppos]
print(host)
dir(str)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos + 3])

text = "X-DSPAM-Confidence:    0.8475"
number = text.find(":")
piece = text[number + 2:]
value = float(piece)
print(value)

# open a file and loop through it
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    # this will skip lines that do not match "From"
    words = line.split()
    print(words[2])

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
#this picks up the second part which comes after the @ symbol
