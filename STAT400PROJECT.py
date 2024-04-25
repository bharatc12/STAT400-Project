import random
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from scipy.stats import norm
import numpy as np

def main():
    histrogram_creator(10, 1000, coin_flip(10))
    histrogram_creator(20, 1000, coin_flip(20))
    histrogram_creator(40, 1000, coin_flip(40))
    histrogram_creator(80, 1000, coin_flip(80))
    histrogram_creator(10, 1000, dice_roll(10))
    histrogram_creator(20, 1000, dice_roll(20))
    histrogram_creator(40, 1000, dice_roll(40))
    histrogram_creator(80, 1000, dice_roll(80))

def coin_flip(n):
    flip_result_vector = []  
    for j in range (1,n):
        random_variable_s = 0
        for i in range(1, 1000):
            flip_result = random.randint(0, 1)
            random_variable_s = random_variable_s + flip_result
        flip_result_vector.append(random_variable_s)
    return flip_result_vector


def dice_roll(n):
    roll_result_vector = []  
    for j in range (1,n):
        random_variable_t = 0
        for i in range(1, 1000):
            roll_result = random.randint(0, 1)
            random_variable_s = random_variable_t + roll_result
        roll_result_vector.append(random_variable_t)
    return roll_result_vector


def histrogram_creator(bins_n, points, result_vector):
    plt.hist(result_vector, bins=bins_n, color='skyblue', edgecolor='black')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Tuple Data')
    mu, sigma = np.mean(result_vector), np.std(result_vector)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, norm.pdf(x, mu, sigma), 'r-', lw=2)
    plt.show()


#Answer for number 4
#The normal curve approximations are the best on the histograms associated with greater n values
    






    
