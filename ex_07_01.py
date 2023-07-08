file_name = input("Enter file name")
file_handle = open(file_name)
print(file_handle)
for lines in file_handle:
    clean = lines.rstrip()
    print(clean.upper())
