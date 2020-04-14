# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[cur_index], arr[smallest_index] = (
            arr[smallest_index], arr[cur_index])
        # TO-DO: swap
    return arr


# print(selection_sort([3, 4, 9, 2, 10, 25, 6]))

# TO-DO:  implement the Bubble Sort function below


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


def bubble_sort(arr):
    arr_size = len(arr) - 1
    for i in range(arr_size):
        for j in range(arr_size - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = temp
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# old way


def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

# new way


def swap_function(arr, idx1, idx2):
    [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]]


print(bubble_sort([9, 3, 4, 5, 6, 3, 1, 2, 44, 11, 8, 33]))


# optimized bubble_sort

def opti_bubble_sort(arr):
    arr_size = len(arr) - 1
    no_swaps = True
    for i in range(arr_size):
        for j in range(arr_size - i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                no_swaps = False
        if no_swaps:
            break
    return arr


print(opti_bubble_sort([99, 34, 2345, 566767,
                        3454545, 56, 78, 12, 34, 454, 2, 1, 4, 5, 7]))


def insertion_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            # shift left until correct position found
            arr[j] = arr[j - 1]
            j -= 1
        # insert at correct position
        arr[j] = temp

    return arr
