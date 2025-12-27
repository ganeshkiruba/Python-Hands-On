#1. Local variable
def order():
    food="Donut"# Local variable cannot be accesed outside this function
    print("Your Order is ",food)
#print(food)---> It returns error.not defined
order()

#2. Enclosed variable
def card():
    discount=10

    def checkout():
        print("Applying discount:",discount)# uses variable within enclosed scope->parent function
    checkout()
card()

#3. Global variable
userid= "ganesh123" # global variable accessed by any function

def user():
    print("User id is ",userid)

def profile():
    print("Welcome !",userid)

user()
profile()

#4. Builtin Variables -> Similar to builtin functions

print(__file__)# displays filename with folder location


