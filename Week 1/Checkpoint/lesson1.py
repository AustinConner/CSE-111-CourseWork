"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = input("Please enter your age: ")
age = int(age)

max_heartrate = 220 - age

lower_heartrate = 0.65 * max_heartrate
upper_heartrate = 0.85 * max_heartrate

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lower_heartrate:.0f} and {upper_heartrate:.0f} beats per minute.")