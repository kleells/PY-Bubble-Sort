# write your bubble sort algorithm below
# Define a function named bubble_sort that takes in a
# list, lst, as a parameter.
def bubble_sort(lst):
    # Write a FOR loop to run the bubble sort algorithm
    # as many times as there are elements in the list
    # (one less than the length of the list). This will be
    # the outer loop.
    for i in range(len(lst)-1):
        # use swapped to make more efficient
        swapped = False
        print(f"iteration ")
        for j in range(len(lst) - 1):
            print(f"comparing {lst[j], lst[j+1]}")
            # Write a conditional statement in the inner loop that
            # checks if the element on the left is greater
            # than the element on the right. If it is, switch
            # the order of the elements.
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True

            if not swapped:
                return
        # Return the value of the lst after it has been sorted
        return lst
# TEST ABOVE ALGORITHM
sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
