import csv
from datetime import datetime, timedelta

def calc_return_policy(date_time, total_days):
    days_in_future = timedelta(days=total_days)
    calc = date_time + days_in_future
    formatted_current_date_and_time = f"{calc:%a %b %d %H:%M:%S %Y}"
    return formatted_current_date_and_time

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
    # Customize Receipt ==========================================================================
    store_name = "YouWishMart"
    sales_tax = 0.06 # sales tax percentage written as a decimal
    thank_you_msg = f"Thank you for shopping at {store_name}! Our prices are actually real!"
    current_date_and_time = datetime.now()
    formatted_current_date_and_time = f"{current_date_and_time:%a %b %d %H:%M:%S %Y}"
    # ============================================================================================


    # create dictonary for products
    products_dict = read_dictionary(r"products.csv", 0)
    # count total purchases
    total_items = 0
    subtotal = 0
    try:
        print(f"{store_name} \n")
        with open(r"request.csv", mode="rt") as requests:
            requests = csv.reader(requests)
            next(requests) # skips header
            for line in requests:
                product_data = products_dict[line[0]]
                product_name = product_data[0]
                product_price = product_data[1]
                requested_quantity = line[1]
                total_items += int(requested_quantity)
                subtotal += float(product_price) * int(requested_quantity)
                print(f"{product_name}: {requested_quantity} @ ${product_price}")
                
            # total items
            print(f"\nNumber of Items: {total_items}")
            
            # subtotal
            subtotal = round(subtotal, 2)
            print(f"Subtotal: ${subtotal}")
            
            # calculate sales tax
            sales_tax = sales_tax * subtotal
            sales_tax = round(sales_tax, 2)
            print(f"Sales Tax: ${sales_tax}")

            # complete total
            print(f"Total: ${subtotal + sales_tax} \n")

            # print msg
            print(thank_you_msg)
            print(formatted_current_date_and_time)

            # return policy
            print(f"\nProduct must be returned by {calc_return_policy(current_date_and_time, 7)} for full refund.")

    except FileNotFoundError as fe:
        print("Error: missing file")
        print(fe)
    except KeyError as ke:
        print("Error: Unknown product ID in the request.csv file.")
        print(ke)

if __name__ == "__main__":
    main() 