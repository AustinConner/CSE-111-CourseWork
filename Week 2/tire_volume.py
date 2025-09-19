import math # for pi
from datetime import datetime # for calculating current date

# get date
current_date_and_time = datetime.now()
current_date = (f"{current_date_and_time:%Y-%m-%d}")

# Width
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))

# Aspect Ratio
tire_aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))

# Diameter
tire_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# calculate volume of air in tire 
calc = math.pi * tire_width ** 2 * tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * tire_diameter) / 10000000000
calc = round(calc, 2)

print (f"The approximate volume is {calc} liters")

def signup():
    user_response = input("Would you like to purchase the tires with the dimensions you specified? (Y/N): ")
    user_response = user_response.lower()
    if user_response == "y":
        print("Awesome! We can give you a call when we have some in stock!")
        phone_number = input("What is a good phone number we can reach you by? ")
        print("We'll be in touch!")
        return phone_number
    elif user_response == "n":
        print("No worries! See you soon!")
    else:
        print("invalid response. Try again. Valid options: 'y', Y, 'n', 'N'")
        signup()

user_contact = signup()

if user_contact:
    pass
else:
    user_contact = "none"

# write results to txt file
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date}, {tire_width}, {tire_aspect_ratio}, {tire_diameter}, {calc}, {user_contact}", file=volumes_file)