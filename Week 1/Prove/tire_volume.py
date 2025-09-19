import math # for pi

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