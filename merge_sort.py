def merge_sort(arr):

    # check if array has more than one element
    if len(arr) > 1:

        # splt arrays into two
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursively call function in the two arrays
        merge_sort(left_arr)
        merge_sort(right_arr)

        # sort:
        i = 0 # index on left array
        j = 0 # index on right array
        k = 0 # index on merged array

        while i < len(left_arr) and j < len(right_arr):
            # Compare items in both arrays, assuming matched indices
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        # if left is loner i.e. i > j
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        # if right is longer i.e. i < j
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


test_array = [4,5,2,7,9,1,3,0,4,2,3,5]
print(merge_sort(test_array))
