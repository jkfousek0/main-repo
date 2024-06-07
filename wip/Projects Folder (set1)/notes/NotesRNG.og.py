
import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)

# Select a random element from a list
elements = ['a', 'b', 'c', 'd']
random_choice = random.choice(elements)

# Generate a random float between 0 and 1
random_float = random.random()

# Generate a random float between 5.0 and 10.0
random_uniform = random.uniform(5.0, 10.0)

# Shuffle a list randomly
random.shuffle(elements)

# Printing results for demonstration
print("Random Integer:", random_integer)
print("Random Choice:", random_choice)
print("Random Float:", random_float)
print("Random Float (5.0 to 10.0):", random_uniform)