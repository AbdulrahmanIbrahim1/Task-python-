def create_histogram(numbers):
    for num in numbers:
        histogram_line = '*' * num
        print(histogram_line)
        
numbers = [2, 5, 3, 8, 4]
create_histogram(numbers)
# -----------------other solution-----------------------------
import matplotlib.pyplot as plt
def create_histogram(numbers):
    plt.hist(numbers, bins=len(numbers))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Integers')
    plt.show()

numbers = [2, 5, 3, 8, 4]
create_histogram(numbers)
