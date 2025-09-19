"""
optional - puzzle
- Write a program that asks the user for a value of n.

- Display 2 matrices of values based on n.
 
For Example:
 
n = 4
 
first one:
 
1  2  3  4

5  6  7  8

9 10 11 12

13 14 15 16
 
second one:
 
1  5  9 13

2  6 10 14

3  7 11 15

4  8 12 16
 
Extra Shape (square with side = n)
 
****

*  *

*  *

****
 
Harder one:
 
n = 6
 
******

*    *

* ** *

* ** *

*    *

******




F2 while highlighting varable allows for easy mass rename/

Ctrl D = Multiple cursors

add cursor to line ends.

We can set keyboard shortcuts to run python script.
"""

# get input
value = int(input("enter value: "))

shape_width = value
shape_height = value
matrix1_counter = 0

# generate first.
while matrix1_counter < value:
    for i in range(shape_width):
        print(i + 1, end=" ")
    print()
    matrix1_counter += 1

# generate second.
matrix2_counter = 0
matrix2_last_value = 0

print(f"value = {value}")
while matrix2_counter < value:
    for i in range(shape_width):
        print(value + matrix2_last_value, end=" ")
        matrix2_last_value += value
    print()
    matrix2_counter += 1

# # create matrix.
# for i in range(value + 1): # +1 because counting starts at 0