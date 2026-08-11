import numpy as np

user_input = input("Enter numbers separated by spaces: ")
numbers = [float(x) for x in user_input.split()]
numbers = np.array(numbers)

print("\n----Array Statistics----")
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation: {std:.2f}".format(std=np.std(numbers)))
print("Min:", np.min(numbers))
print("Max:", np.max(numbers))
