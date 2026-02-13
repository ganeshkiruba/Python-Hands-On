age = 101
# if else
if age>= 18:
    print("You can vote")
else:
    print("Not Eligible to vote!!!")


#multiple ifs
mark = 75
if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 70:
    print("Grade C")
else:
    print("Grade D")

has_licence = False
# nested if 
if age>= 18:
    if has_licence == True:
        print("Eligible to Driver")
    else:
        print("Take License to Drive")
else:
    print("Not eligible to drive")

#multiple condition check in same if
if age >=25 and mark >= 80:
    print("Good Progress")
elif age >=50 or mark <=50:
    print("Improve!!!")
else:
    print("No Commentts!!")

order_amt = 100
day = "saturday"
membership = "no"

if(order_amt>=1000 and day in['saturday','sunday']) or membership =='gold':
    print("Discount Eligible")
else:
    print("No Discount")