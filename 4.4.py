def main():
    count = 0

    while count < 5:
        print("Inside the while loop:", count)
        count += 1
        if count == 3:
            break
    else:
        print("Inside the else block of the while loop")

    print("Outside the while loop")

if __name__ == "__main__":
    main()