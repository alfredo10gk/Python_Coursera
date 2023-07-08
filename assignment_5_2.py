largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number
    except ValueError:
        print("Invalid input")
        continue

if largest is not None and smallest is not None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
else:
    print("No valid numbers entered.")
    
#    try {
        largest = None
        smallest = None
        while True:
        num = input("Enter a number: ")
        if num == "done":
        break
        try:
        number = int(num)
        if largest is None or number > largest :
        largest = number
        if smallest is None or number < smallest :
        samllest = number
        except ValueError :
        print("Invalid input")
        continue
        if largest is not None and smallest is not None :
        print("Maximum is", largest)
        print("Minimum is", smallest)
        else :
        print("No valid numbers entered")
  #  } catch (e) {
#        //Catch Statement
 #   }