name = "ganeshkiruba SHANKAR"

print(name.upper())
print(name.lower())
print(name.capitalize())


mobile = "9876543210"
# only first 2 digts
masked = mobile[:2]+"********"
# only last 2 digits
masked2 = "********"+ mobile[-2:]

# masked except first2 and last 2
masked3 =   mobile[:2]+"******"+mobile[-2:]

print(masked)
print(masked2)
print(masked3)

song = "shape OF yoU"
artist = "Eminem"
formatted = f"{song.title()} - {artist.title()}"
print(formatted)

location = "chennai central"
fixed_location = location.replace("chennai central","Tambaram")
print(fixed_location)

message = "Your Uber Booking id is: UB12345. Please keep it safe!"
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)


promo_msg = "use zomoto100 to get 100 off on your order"
if "zomoto100" in promo_msg:
    print("offer applied!")

feedback = "the driver was polite and the ride was smooth"
print("position is :", feedback.find("polite"))

#single line for loop
new_name = "ganeshkirubashankar pavadaisamy"
initals = "".join([word[0].upper() for word in new_name.split()])
print(initals)

dirty_input = "   Hello!    "
clean = dirty_input.strip()
print(clean)

word1 ="the trip was amazing and the car is clean"
word_count = len(word1.split(""))
print(word_count)