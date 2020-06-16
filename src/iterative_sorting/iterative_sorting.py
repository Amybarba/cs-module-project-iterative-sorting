# TO-DO: Complete the selection_sort() function below
from typing import List


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


data = [7, 6, 9, 13, 2, 5, 11, 22]

print(selection_sort(data))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # Outer Loop
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also would work but outer loop will repeat one time
        # i elements are in place
        for j in range(0, n - i - 1):
            # traverse the array from index 0 to n-i-1
            # swap if the element found is greater
            # then move to the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


bubble_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bubble_sort(bubble_data))

"""Alternative solution:


def bubble_sort(arr):
    swap_numbers = True
    while swap_numbers:
        swap_numbers = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # swap numbers
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap_numbers = True

    return arr"""

'''
STRETCH: implement the Count Sort function below

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
'''


# def counting_sort(arr, maximum=None):
# Your code here


# return arr

# counting_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(counting_sort(counting_data))
def count_sort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i - 1]

        # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


# Driver google StackOverflow to test above function
arr = "geeksforgeeks"
ans = count_sort(arr)
print("Sorted character array is %s" % ("".join(ans)))
