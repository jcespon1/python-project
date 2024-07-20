name = input("what is your name? ")
print ("welcome " + name)
score = 0

answer1 = input("what is chocolate made from? ")
if answer1 == "cocoa":
    print ("correct")
    score = score + 1
else:
    print('incorrect, the answer is cocoa')

answer2 = input("what country is the Philippines from? ")
if answer2 == "asia":
    print('correct')
    score = score + 1
else:
    print('incorrect answer, its Asia')

answer3 = input("Does Mango Taste good? ")
if answer3 == "yes":
    print('correct')
    score = score + 1
else:
    print('you wrong ma boi')

answer4 = input("Is Ed Sheeran british? ")
if answer4 == "yes":
    print('correct')
    score = score + 1
else:
    print('how you get this wrong?')

answer5 = input("Favourite Michael Jackson song? ")
if answer5 == "beat it":
    print('correct')
    score = score + 1
else:
    print('you are wrong, this is not a debate')

print('contrats you got ', score)






