def main():

    numbers = [10, 32, 24, 47, 8, 18]

    updated_numbers = list(map(transform_number, numbers))

    print(updated_numbers)

def transform_number(num):

    return num * 1.1 if num > 20 else num * 0.9

if __name__ == "__main__":

    main()

# [9.0, 35.2, 26.400000000000002, 51.7, 7.2, 16.2]

# python main.py
