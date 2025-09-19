import random
from words_list import get_random_word
def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        # generate random number
        random_number = random.uniform(1,100)
        # round to nearest 10s place
        random_number = round(random_number, 1)
        # Append number to list
        numbers_list.append(random_number)
         
def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"Base numbers list: {numbers}")
    append_random_numbers(numbers)
    print(f"1 number appended: {numbers}")
    append_random_numbers(numbers, 3)
    print(f"3 numbers appended: {numbers}")

    words_list = []
    print(f"Empty list: words_list")
    append_random_words(words_list)
    print(f"1 word appened: {words_list}")
    append_random_words(words_list, 3)
    print(f"3 words appended: {words_list}")

    

def append_random_words(words_list, quantity=1):
    for _ in range(quantity):
        # get random word
        word = get_random_word()
        # append word
        words_list.append(word)

    

if __name__ == "__main__":
    main()