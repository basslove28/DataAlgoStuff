            #SORTING ALGORITHMS
#This is how you create an Insertion sort
'''
#Insertion Sort method:
def insertion_sort(unordered_list):
    #Takes in the list to be sorted as a parameter
    for i in tyange(1,len(unordered_list)):
        #Start from one since the iteration occurs up tro the length of the list
        j = i -1
        #j is the position of the current element
        #i is the position of the next element.
        next_element = unordered_list[i]

        while(unordered_list[j] > next_element) and(j >=0):
            #We swap the elements if the current element is larger than the next element.
            unordered_list[j+1] = unordered_list[j]
            j = j -1
        #We move to the next element.
        unordered_list[j+1] = next_element
    #WE print out the ordered_list but its name is still unordered_list
    print(unordered_list)
'''

#This is how to create a Bubble sort
'''
#Bubble sort method:
def bubblesort(unordered_list):
    #Takes in the list to be sorted as a parameter.
    for num in range(len(unordered_list)-1,0,-1):
        #We iterate over the positions in the list.
        #We start with the last element and move leftwards, one step upto the first element.
        for idx in range(num):
            #We take a position 'idx' in the list to compare with the adjacent numbes.
            if unordered_list[idx] > unordered_list[idx+1]:
                #We swap the numbers if they're not in order.
                temp = unordered_list[idx]
                unordered_list[idx] = unordered_list[idx+1]
                unordered_list[idx+1] = temp
    #We print out the ordered list but retained its name which was 'unordered_lis'
    print(unordered_list)
'''

#This is how to create a Selection sort
'''
#Selection sort method.
def selection_sort(unordered_list):
    #The function takes the list to be sorted as a parameter.
    for idx in range(len(unordered_list)):
        #We take the position 'idx' for the lenght of the list.
        min_idx = idx
        #We assume the position of the smallest element is idx hence min_idx.
        for j in range(idx+1, len(unordered_list)):
            if unordered_list[min_idx] > unordered_list[j]:
                #We check if it is indeed the smallest number and record its position
                min_idx = j
        #We swap the elements so that they can be in order
        unordered_list[idx], unordered_list[min_idx] = unordered_list[min_idx], unordered_list[idx]
    #We print out the sorted list but we retained its name as unordered_list
    print(unordered_list)
'''

#This is how to create a Merge sort
'''
# Merge sort method/Function
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the middle of the array
        r = len(arr) // 2

        # Dividing array into two halves
        leftArray = arr[:r]
        rightArray = arr[r:]

        # Calling mergesort function on subparts of array
        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0

        # Copying data to temp arrays leftArray[] and rightArray[]
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1


# function to print the array
def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code
if __name__ == '__main__':
    arr = [6, 5, 12, 10, 9, 1]
    print("Original array")
    display(arr)
    mergeSort(arr)
    print("Sorted array")
    display(arr)
'''

#This is how to create a Quick sort
'''
# The partition function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# Quick sort function
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Driver code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d"%arr[i])
'''

#This is how to implement a Heap sort
'''
def heapify(arr, n, i):
    largest = i  # In max-heap largest is at root
    l = 2 * i + 1  # left child index = 2*i + 1
    r = 2 * i + 2  # right child index = 2*i + 2

    # See if left child of root exists and > root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and > root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # update root if required
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

    # Heapify the root
        heapify(arr, n, largest)

    # heap sort definition


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extracting elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])
'''
           #SEARCHING ALGORITHMS

#This is how to implement a Linear search
'''
#Linear search method.
def linear_search(values, searched):
   #The function takes in only two parameters.
   #'Searched' is the element being looked for.
   #'Values' is the list in which the element is searched.
   for i in range(0, len(values)):
       #We iterate over every element in the list.
       if (values[i] == searched):
           #If we find the element, we return the position of the element in the list.
           return "Element " + str(searched) + " is at " + str(i+1)
   #If we don't find the element, we return an 'absent statement'
   return "Element has not been found"
'''

#This is how to implement a Binary search

'''
#Binary search method.
def binary_search(values, l, r, searched):
    #The fucntion takes four parameters.
    #'Values' is the list in which a value is being searched.
    #'Searched' is the element being looked for.
    #r is the lenght of the list.
    #The lenght of the list keeps on changing every time we split the list
    values.sort()
    #We sort the list since the function needs the list to be sorted.
    if r >= 1:
        #For as long as the lenght of the list is not less than one.
        mid = l + (r - 1) // 2
        #The above line splits the list.
        if values[mid] == searched:
            #We check if the value is the element being searched for.
            return "Element " + str(searched) + " is at " + str(mid+1)
        elif values[mid] > searched:
            #We check if the middle value is bigger than the element being searched.
            return binary_search(values, l, mid-1, searched)
            #We recall the function over the second half.
        else:
            #If the mid value is smaller that the element being searched
            #We recall the fucntion over the first half.
            return binary_search(values, mid+1, r, searched)
    else:
        #If we searched through the list after spliting it several times and failed to get the element, we return an 'absent statement'.
        return "Element is not present in the array"
'''
