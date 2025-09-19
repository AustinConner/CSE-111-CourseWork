def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(fruit_list)
    fruit_list.append("orange")
    print(fruit_list)
    apple_index = fruit_list.index("apple")
    fruit_list.insert(apple_index, "cherry")
    print(fruit_list)
    fruit_list.remove("banana")
    print(fruit_list)
    last_element = fruit_list.pop()
    print(last_element)
    print(fruit_list)
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(fruit_list)

if __name__ == "__main__":
    main()