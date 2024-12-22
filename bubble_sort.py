#binary search looks for te middle number and adjusts accordingly
#for a list n, it will take log n, which is to base 2

def binary_search(list, x):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = round((low + high)/2)
        guess = list[mid]
        if guess == x:
            return mid
        if guess > x:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
x = 1
print(binary_search(my_list, x))