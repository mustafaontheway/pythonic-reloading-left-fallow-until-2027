import numpy as np

def main():

    np.random.seed(100)

    all_ages = np.random.randint(0, 100, 10000)

    mean_all_ages = np.mean(all_ages)

    print(mean_all_ages) # 49.6733

    for i in range(20):

        sm = np.mean(np.random.choice(all_ages, 100))

        print("Sample age mean: ", sm)

if __name__ == "__main__":
    main()

"""
Sample age mean:  51.03
Sample age mean:  47.63
Sample age mean:  46.46
Sample age mean:  51.43
Sample age mean:  42.34
Sample age mean:  46.02
Sample age mean:  49.57
Sample age mean:  50.66
Sample age mean:  47.34
Sample age mean:  44.86
Sample age mean:  49.32
Sample age mean:  46.93
Sample age mean:  49.43
Sample age mean:  47.0
Sample age mean:  50.42
Sample age mean:  48.45
Sample age mean:  48.08
Sample age mean:  45.79
Sample age mean:  48.86
Sample age mean:  52.88
"""

# python main.py
