"""
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping.

Write a Python program named boxes.py that asks the user for two integers:
1. the number of manufactured items
2. the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. 
* Note that the last box may be packed with fewer items than the other boxes. *
"""
import math

def convert_to_int(value):
    if value.isnumeric():
        new_value = int(value)
        return new_value
    else:
        print(f"{value} can't be converted to an interger. Ensure that an interger value is entered.")

total_items = input("Enter the number of items: ")
items_per_box = input("Enter the number of items per box: ")

total_items = convert_to_int(total_items)
items_per_box = convert_to_int(items_per_box)

boxes_needed = math.ceil(total_items / items_per_box)

print(f"For {total_items} items, packing {items_per_box} items in each box, you'll need {boxes_needed} boxes.")