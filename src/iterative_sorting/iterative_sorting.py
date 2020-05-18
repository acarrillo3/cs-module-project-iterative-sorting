# TO-DO: Complete the selection_sort() function below
list = [1, 14, 5, 6, 17, 9, 15, 44, 6, 32]
def selection_sort(arr):
    # How many loops will be needed to complete this algorithm?
    # When to swap values?
    # How to keep track of which values should be swap?
    # loop through n-1 elements
    # for every index in the collection from 0 to length-2:
    for i in range(0, len(arr) - 1):
        # compare the element at the current index, i, with everything on its right to identify
        # Swap the element at i with the smallest element
        # i++
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(smallest_index +1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j


        # TO-DO: swap
        # swap smallest indeex with current index and repeat
        # Your code here
        if cur_index != smallest_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    # return the array sorted
    return arr
print(selection_sort(list))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(1, len(arr)):
        for j in range(0, len(arr) -1):
            if arr[j] > arr [j + 1]:
                arr[j], arr[j +1] = arr[j + 1], arr [j]
    return arr
print(bubble_sort(list))


# STRETCH: implement the Count Sort function below
#def count_sort(arr, maximum=-1):
    # Your code here


#    return arr
