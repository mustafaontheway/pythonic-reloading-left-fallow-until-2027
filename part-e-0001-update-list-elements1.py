def main():

    numbers = [10, 32, 24, 47, 8, 18]

    new_numbers = []

    for number in numbers:

        if number > 20:

            new_numbers.append(number * 1.1)

        else:

            new_numbers.append(number * 0.9)

    print(f"Updated numbers: {new_numbers}")

if __name__ == "__main__":

    main()

# Updated numbers: [9.0, 35.2, 26.400000000000002, 51.7, 7.2, 16.2]
