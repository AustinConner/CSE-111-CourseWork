"""
Get's customer subtoital and then calculates whether or not they get a discount depending on the day of the week.

Requirements:
1. if subtotal is $50 or more and the current day is tuesday or wedensday, they get 10% off.
2. calculate sales tax.
3. print discount (if applicable), sales tax amount, and total amount due.
"""
from datetime import datetime

# # get subtotal from user
subtotal = input("Please enter the subtotal: ")

# # ensure float value
try:
    subtotal = float(subtotal)
except:
    raise SystemExit("Subtotal isn't a number. Run program again with a valid number.")


# calculate day of the week
current_date = datetime.now()
day_as_int = current_date.weekday() # int for the day of the week. Mon = 0, Sun = 7

day_as_int = 2

running_total = subtotal # we will add or take away from this value. This is the new total.

# # calculate discount
discount_percentage = 10
min_purchase_amount = 50

def calc_discount(total):
    total_discount = (total * discount_percentage) / 100
    return total_discount

def under_discount_threshold():
    amt_needed = min_purchase_amount - subtotal
    print(f"You only need to spend ${amt_needed:.2f} to earn a {discount_percentage}% discount!")

# determine if discount applies
discount_applies = None
if day_as_int == 1: # tuesday
    if subtotal >= min_purchase_amount:
        discount_applies = True
    else:
        under_discount_threshold()
elif day_as_int == 2: # wedensday
    if subtotal >= min_purchase_amount:
        discount_applies = True
    else:
        under_discount_threshold()

# calculate discount
if discount_applies:
    total_discount = calc_discount(subtotal)
    print(f"Discount amount: ${total_discount:.2f}")
    running_total -= total_discount

# calculate tax
tax = (running_total * 6) / 100
print(f"Sales tax amount: ${tax:.2f}")
running_total += tax

print(f"Total: ${running_total:.2f}")