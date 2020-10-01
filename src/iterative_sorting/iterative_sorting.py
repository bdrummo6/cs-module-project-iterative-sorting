# TO-DO: Complete the selection_sort() function below
"""
During each iteration of the selection sort algorithm it takes the smallest element and swaps it with the
element in the corresponding position to the left.
"""
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
"""
The bubble_sort algorithm sorts a list of elements by comparing two adjacent elements and swapping them, 
if they are not in the correct order.
"""
def bubble_sort(arr):
    # Starts at the last element and ends at the first element, moving every iteration one element
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
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

print('\nList in original order: ')
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
    # Your code here

    return arr
