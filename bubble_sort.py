def bubble_sort(my_list):
    # Get length of the list
    list_length = len(my_list) - 1

    #Variable to track state of sorted
    is_sorted =  False

    while not is_sorted:
        # Change sorted to true, check to allow breaking from while
        is_sorted = True

        for i in range(0, list_length):
            #check each adjacent pair
            if my_list[i] > my_list[i+1]:
                is_sorted = False
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    return my_list


print(bubble_sort([5,6,7, 4, 2,6, 8, 3, 7]))
