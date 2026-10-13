springp = 0
summerp = 0
winterp = 0
fallp = 0
print ("type answers in lowercase, choose the letter")
answer1 = input ("do you like A, rain B, sun C, snow or D,fall weather")
if answer1 == "a":
    springp += 1
elif answer1 == "b":
    summerp += 1
elif answer1 == "c":
    winterp += 1
elif answer1 == "d":
    fallp += 1

answer2 = input ("do you like to A, go puddle jumping B, go swimming C, skiing or snowboarding or D, trick or treating")
if answer2 == "a":
    springp += 1
elif answer2 == "b":
    summerp += 1
elif answer2 == "c":
    winterp += 1
elif answer2 == "d":
    fallp += 1

answer3 = input ("do you like A, tea B, lemonade C, hot chocolate or D, pumpkin spice latte with 2 pumps of vanilla whipped cream sprinkles and a cake pop")
if answer3 == "a":
    springp += 1
elif answer3 == "b":
    summerp += 1
elif answer3 == "c":
    winterp += 1
elif answer3 == "d":
    fallp += 1

answer4 = input ("do you like A, crisp mornings B, hot mornings C, cold mornings or D, crisp and cold mornings")
if answer4 == "a" or answer4 == "A":
    springp += 1
elif answer4 == "b":
    summerp += 1
elif answer4 == "c":
    winterp += 1
elif answer4 == "d":
    fallp += 1

answer5 = input ("do you like A, soccer B, swimming C, skiing or D, basketball")
if answer5 == "a" or answer4 == "A":
    springp += 1
elif answer5 == "b":
    summerp += 1
elif answer5 == "c":
    winterp += 1
elif answer5 == "d":
    fallp += 1

#spring ending you like spring activities
if springp > summerp and springp > winterp and springp > fallp :
    print ("you are a spring person")

#summer ending you like summer activities
if summerp > springp and summerp > winterp and summerp > fallp :
    print ("you are a summer person")

#winter ending you like winter activities
if winterp > summerp and winterp > springp and winterp > fallp :
    print ("you are a winter person")

#fall ending you fall spring activities
if fallp > summerp and fallp > winterp and fallp > springp :
    print ("you are a fall person")