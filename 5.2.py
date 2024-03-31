def main():
    my_list = ['q', 'w', 'e', 'r', 't', 'y']

    print("Printing elements of the list along with indexes:")
    for i, item in enumerate(my_list):
        print(f"Element: {item}, Positive Index: {i}, Negative Index: {-len(my_list) + i}")

if __name__ == "__main__":
    main()
