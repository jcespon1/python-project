sh = input("Amount of hours")
sr = input("Amount of pay")
fh = float(sh)
fr = float(sr)
print(fh, fr)
if fh > 40:
    print("Overtime")
    reg = fr*fh
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg,otp)
    xp = reg+otp
else:
    print("regular")
    xp = fh * fr
print("Pay:",xp)

