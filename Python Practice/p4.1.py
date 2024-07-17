sh = input("Amount of hours")
sr = input("Amount of pay")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("error, please enter numeric input")
    
print(fh, fr)
if fh > 40:
    reg = fr*fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg+otp
else:
    xp = fh * fr
print("Pay:",xp)
