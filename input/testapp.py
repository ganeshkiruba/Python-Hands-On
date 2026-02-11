import sys

if len(sys.argv) == 2:
    print("Usage:Python emailgenerator.py 'FUll and Last name")
    sys.exit()

full_name = " ".join(sys.argv[1:])

#email format from full_name

email = full_name.lower().replace( " ",".")+ "@company.com"
print("\n ----Profile----")
print("Full Name:", full_name)
print("Generated Email:",email)