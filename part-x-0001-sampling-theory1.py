import numpy as np

def main():

    np.random.seed(100)

    all_ages = np.random.randint(0, 100, 10000)

    mean_all_ages = np.mean(all_ages)

    print(mean_all_ages) # 49.6733

    ages_sample1 = np.random.choice(all_ages, 100)

    ages_sample2 = np.random.choice(all_ages, 100)

    print(np.mean(ages_sample1)) # 51.03

    print(np.mean(ages_sample2)) # 47.63


if __name__ == "__main__":
    main()

# python main.py
