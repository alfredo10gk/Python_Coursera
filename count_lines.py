# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
   if line.startswith("X-DSPAM-Confidence:"):
        value = float(line[line.find(":") + 1:].strip())
        count += 1
        total += value
fh.close()
average = total / count
print("Average spam confidence:", average)