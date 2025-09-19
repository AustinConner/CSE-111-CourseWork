import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    i_num_dict = {}
    with open(filename, mode="rt") as i_num_csv:
        # read the csv file with the csv module
        reader = csv.reader(i_num_csv)
        next(reader) # goes down a line in the csv essentially from the top. this skips the header.
        for key, value in reader:
            i_num_dict[key] = value

    return i_num_dict

def find_i_num(i_num, dict):
    if i_num in dict:
        student = dict[i_num]
        return student
    else:
        False

def verify_i_number(i_number):
    if len(i_number) == 9:
        return False
    elif len(i_number) > 9:
            error = "Invalid I-Number: too many digits"
    elif len(i_number) < 9:
            error = "Invalid I-Number: too few digits"
    elif not i_number.isalnum():
            error = "Invalid I-Number: invalid char"
    return error

if __name__ == "__main__":
    # get i number from user.
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    # remove dashes
    i_number = i_number.replace("-", "")

    i_number_check = verify_i_number(i_number)
    if i_number_check:
         print(i_number_check)


    i_num_dict = read_dictionary(r"C:\Users\alcon\OneDrive - BYU-Idaho\Classes\2025\Spring\CSE 111\Week 9\students.csv")
    i_num_search = find_i_num(i_number, i_num_dict)
    if i_num_search:
        print(i_num_search)
    else:
        print("No such student")
        