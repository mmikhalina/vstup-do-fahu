import numpy as np
import random

table = []
# generate table 11*4 appending to table lists of 4 random elements
for i in range(11):
    tmp_array = [random.randint(15, 30) for i in range(4)]
    table.append(tmp_array)


# display table data
print("           A   B   C   D")      # mark columns with class letters
class_ = 1      # the class  number
for row in table:  # row is equal to list of 4 elements
    print("\033[31m {}" .format(""), "\n", class_, "class:", end=" ")  # "\033[31m {}".format("") - set text color to red
    for element in row:  # get each element from the row
        print("\033[37m {}" .format(""), element, sep="", end=" ")  # "\033[37m {}".format("") - set text color to grey
    class_ += 1     # increase the current class  number

print("\n--==--")

# looking for the minimum elements for each parallel classes
class_ = 1
for row in table:  # the row contains all parallel classes
    print("Min in", class_, "classes - ", min(row))  # using min() function
    class_ += 1  # increase the current class  number again

print("\n--==--")

tmp_array = []  # it will be contain columns
letters = ["A", "B", "C", "D"]  # to display letter of column
for i in range(4):  # "i" is letter (1-A, 2-B etc.)
    for j in range(11):  # get elements in the column to tmp_array
        tmp_array.append(table[j][i])  # add each element of current column to array
    print("Min in", letters[i], "classes - ", min(tmp_array))
    tmp_array.clear()  # clear the current column to write down here the new column
