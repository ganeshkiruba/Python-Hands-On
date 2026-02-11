a=10
b=3
#Arithmetics
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) # 10*10*10
print(a//b)
#Comparison
x=5
y=20
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
#logical
g=True
v=False
print(g and v)
print(g or v)
print(not g)


print("----------operator example-----------")
amount = 1200
tax = amount *0.18
total=amount + tax
print(total)
if total >1000:
    discount = total*0.10
    total -= discount
print(total)

print("-------")
age =65
student ='yes'

if age>=60 or student =='yes':
    print("Yes Discount")
else:
    print("No Discount")


# Single line comment

'''
Block Comments/ Multi line comment
'''
"""
Muti line/Block comment
"""