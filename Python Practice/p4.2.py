def computepay(hours, rate) :
    ##print("In computepay", hours, rate)
    if fh > 40:
        reg = fr*fh
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg+otp
    else:
        pay = hours * rate
    print("Returning",pay)
    return pay
    

sh = input("Amount of hours")
sr = input("Amount of pay")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay:",xp)
