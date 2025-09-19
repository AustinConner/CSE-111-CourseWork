import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # indexs
    KCI = key_column_index
    NAME = 1
    PRICE = 2
    with open(filename, mode="rt") as raw_csv:
        csv_clean = csv.reader(raw_csv)
        next(csv_clean)
        converted_dictonary = {}
        for line in csv_clean:
            key = line[KCI]
            name = line[NAME]
            price = line[PRICE]

            # add values to dictonary
            converted_dictonary[key] = [name, price]

        return converted_dictonary

def main():
    # create dictonary for products
    products_dict = read_dictionary(r"products.csv", 0)
    print(products_dict)

    # Read requests
    with open(r"request.csv", mode="rt") as requests:
        requests = csv.reader(requests)
        next(requests) # skips header
        for line in requests:
            product_data = products_dict[line[0]]
            product_name = product_data[0]
            product_price = product_data[1]
            requested_quantity = line[1]
            print(f"{product_name}: {requested_quantity} @ ${product_price}")

            

if __name__ == "__main__":
    main()