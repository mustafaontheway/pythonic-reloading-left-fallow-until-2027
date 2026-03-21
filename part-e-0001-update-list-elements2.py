def main():

    numbers = [10, 32, 24, 47, 8, 18]

    new_numbers = [number * 1.1 if number > 20 else number * 0.9 for number in numbers]

    print(f"Updated numbers: {new_numbers}")

    print(f"Updated numbers: {[round(num, 3) for num in new_numbers]}")

if __name__ == "__main__":

    main()

# Updated numbers: [9.0, 35.2, 26.400000000000002, 51.7, 7.2, 16.2]
# Updated numbers: [9.0, 35.2, 26.4, 51.7, 7.2, 16.2]

# python main.py
