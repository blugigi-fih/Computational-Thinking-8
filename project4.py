print ("i am help bot")
homework = ("history")
history_grade = ("c")
comp_grade = ("a")

#loop for lines 7 to 20
for i in range (6) :
    choice = input ("what do you want to check. grades homework or weekend schedule.")

    if choice == "grades":
        print (f"your grades are {history_grade} in history")
        print (f"your grades are {comp_grade} in comp")

    elif choice == "weekend schedule":
        print ("you have lacrosse on saturday and sunday and soccer on saturday")

    elif choice == "homework":
        print (f"your homework is {homework}")
        homework = input (" homework update")
    else:
        print ("be sure to choose one of the options")
print ("thank you your fee of 10 dollars will be sent to you shortly")
print ("you should give me money")
money = input ("how much money")
if money > ("10"):
    print ("hooray!!!!")