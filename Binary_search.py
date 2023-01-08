#Function: binary_search
#This function takes a sorted array and an item. If the item is in the array, the function returns its position.

def binary_search(list, item):
    low = 0
    high = len(list)-1
    count = 0
    while low<=high:
        mid = (low + high) // 2
        guess = list[mid]
        count+=1

        if guess == item:
            return mid, count

        if guess > item:
            high = mid -1

        else:
            low = mid + 1

    return None

my_list = [i for i in range(501)]
print('The number is in: ', binary_search(my_list, 250)[1])






