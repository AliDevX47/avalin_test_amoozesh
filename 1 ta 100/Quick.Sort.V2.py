
import random

# Generate random numbers from 1 to 100
random_numbers = random.sample(range(1, 101), 100)
print("Random Numbers:", random_numbers)

# Quick sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Sort the random numbers in ascending order
sorted_numbers = quick_sort(random_numbers)

print("\nSorted Numbers (Ascending):", sorted_numbers)
