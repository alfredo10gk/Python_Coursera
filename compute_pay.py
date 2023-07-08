def computepay(hours, rate):
    if hours > 40:
        regpay = 40 * rate
        ovtpay = (hours - 40) * (rate * 1.5)
        total_pay = regpay + ovtpay
    else:
        total_pay = hours * rate
    return total_pay

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = computepay(hours, rate)
print("Pay", pay)

# this is my errorneous code 
#def computepay(hours, rate):
 #   if hours > 40 :
  #      regpay = hours*rate
   #     ovtpay = (hours-40)*(rate*1.5)
    #    xpay = regpay + ovtpay
    #else:
     #   total_pay = hours * rate 
      #  return total_pay
    
#hours = float(input("Enter Hours:"))
#rate = float(input("Enter Rate:"))
#pay = computepay(hours,rate)
#print("Pay", pay)