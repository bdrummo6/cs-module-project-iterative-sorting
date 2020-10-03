# TO-DO: Complete the selection_sort() function below
"""
During each iteration of the selection sort algorithm it takes the smallest element and swaps it with the
element in the corresponding position to the left.
"""
def selection_sort(arr):
    for i in range(len(arr)-1):
        smaller_i = i
        # Starting with the current index comparing the element at smallest_i with all of the elements in arr
        for j in range(i, len(arr)):
            # if the element at smallest_i is greater than the one at j then j becomes the new smallest_i
            if arr[j] < arr[smaller_i]:
                smaller_i = j

        # Swapping the elements with the current index and current smallest index
        arr[i], arr[smaller_i] = arr[smaller_i], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
"""
The bubble_sort algorithm sorts a list of elements by comparing two adjacent elements and swapping them, 
if they are not in the correct order.
"""
def bubble_sort(arr):
    # At the end of a loop the largest value will be at the current last index, and will not be iterated through again
    for i in range(len(arr)-1, 0, -1):
        # loops through arr starting at 0 and stops at the current value of i
        for j in range(i):
            # if the value at j is greater than the value at the next index, then swap values
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


"""
# Selection Sort Testing

s_list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]  # Create list for sorting

print('\nList in original order: ')
print(s_list)  # Prints list in original order: [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

selection_sort(s_list)  # Call selection_sort function on list

print('\nList after sorted using the selection_sort function: ')
print(s_list)  # Print sorted list
print()


# Bubble Sort Testing

b_list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]  # Create list for sorting

print('List in original order: ')
print(b_list)  # Prints list in original order: [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print('\nList after sorted using the bubble_sort function: ')
bubble_sort(b_list)

print(b_list)
"""


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""

def counting_sort(arr, maximum=None):
    # Check if the list is empty and returns and empty list if so
    if not arr:
        return []
    # If maximum is None then set calculate the maximum value in the list
    if not maximum:
        maximum = max(arr)

    # Creates a list of 0s the length of the maximum value of arr+1
    count = [0 for _ in range(maximum+1)]

    # Sums the number each value in arr and stores that number at the index corresponding to each value
    for i in arr:
        # Checks if a value in arr is negative and if so returns error message
        if i < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        count[i] += 1

    curr_index = 0
    for j in range(maximum+1):
        for k in range(count[j]):
            arr[curr_index] = j
            curr_index += 1

    return arr

