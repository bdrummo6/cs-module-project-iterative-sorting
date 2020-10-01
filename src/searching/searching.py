def linear_search(arr, target):
    # loops through the list
    for i in range(len(arr)):
        # If an element in the list is equal to the target then return the element's index
        if arr[i] == target:
            return i  # target value found in list (arr)

    return -1  # target value not found in list (arr)


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Initialize the first and last values for keeping track of the start and end indices of the current list
    first = 0
    last = (len(arr) - 1)

    # loops until the first is greater than the last or target is equal to the current middle element value
    while first <= last:
        # Use floor division to get the current middle element's index
        mid = (first + last) // 2

        # if the middle element is equal to the element we are searching for return the element's index
        if arr[mid] == target:
            return mid  # target value found in list (arr)
        # if the middle element is not equal to target
        else:
            # if the target value is less than the middle element's then search to the left of the middle element
            if target < arr[mid]:
                last = mid - 1
            # if the target value is more than the middle element's then search to the right of the middle element
            else:
                first = mid + 1

    return -1  # target value not found in list (arr)
