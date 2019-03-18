def bubble_sort(items):
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):

                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items
    '''Return array of items, sorted in ascending order'''
def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result



    '''Return array of items, sorted in ascending order'''
def quick_sort(items):
    if len(items) == 2:
        if items[0] > items[1]:
            return [items[1], items[0]]
        else:
            return items
    else:
        pivot_val = items[0]
        left_list = []
        right_list = []
        equal_list = []

        for idx in range(len(items)):
            if items[idx] == pivot_val:
                equal_list.append(items[idx])
            elif items[idx] < pivot_val:
                left_list.append(items[idx])
            else:
                right_list.append(items[idx])

        if len(left_list) > 1:
            left_list = quick_sort(left_list)
        if len(right_list) > 1:
            right_list = quick_sort(right_list)

        return_list = left_list + equal_list + right_list

    return return_list
