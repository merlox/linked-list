# -*- encoding: utf-8 -*-

def merge_sort(list):
    '''
    Sorts a list using the merge sort algorithm, the steps are the following:
    Divide: divides the list into subarrays by halving each part
    Compare: compares each subarray to its closest neighbour
    Join: joins the list back and sorts again for the subsets

    Splitting recursively is a Logarithmic Time operation O(log n) because we are splitting in halves
    for the entire list.
    Now because we are also using merge, which is a Linear Time operation O(n), the resulting
    runtime of merge_sort is O(n log n)
    But because the split [:] function in python takes O(k), the entire costs is:
    O(nk log n)

    The space complexity is N because we keep all the elements at the same time once in memory in the worst case
    Linear Space Complexity O(n)
    '''

    if len(list) <= 1:
        return list

    left_split, right_split = split(list)
    left = merge_sort(left_split)
    right = merge_sort(right_split)

    return merge(left, right)

def split(list):
    '''
    Returns the split array
    This is a constant time operation O(1)
    '''
    midpoint = len(list) / 2
    left = list[:midpoint]
    right = list[midpoint:]
    return left, right

def merge(a, b):
    '''
    Receives two arrays, sorts them based on size and merges them
    This is a Linear Time operation O(n) because in the worst case we have to check every element
    '''
    sorted = []
    left_index = 0
    right_index = 0

    while left_index < len(a) and right_index < len(b):
        if a[left_index] < b[right_index]:
            sorted.append(a[left_index])
            left_index += 1
        else:
            sorted.append(b[right_index])
            right_index += 1

    # If the left array contains more than 1 element, continue adding those elements
    while left_index < len(a):
        sorted.append(a[left_index])
        left_index += 1

    # If the right array contains more than 1 element, continue adding those elements
    while right_index < len(b):
        sorted.append(b[right_index])
        right_index += 1

    return sorted

def verify_list(list):
    '''
    Verify that a list is correctly sorted recursively
    It checks each pair of elements, then moves to the next pair recursively until it's complete

    This is a Linear Runtime operation O(n) because we need to check every single element
    '''
    # Check the first 2 elements, delete the first one
    if len(list) <= 1:
        return True
    else:
        return list[0] <= list[1] and verify_list(list[1:])

    # Without recursion
    # last_element = -float('inf')
    # for element in list:
    #     if last_element > element:
    #         return False
    #     last_element = element
    # return True


example_list = [19, 22, 13, 291, 35, 83, 55, 49, 2, 353, 423]
print('Original', example_list)
print('Sorted', merge_sort(example_list))
print('Verify list one', verify_list(example_list))
print('Verify list two', verify_list(merge_sort(example_list)))
