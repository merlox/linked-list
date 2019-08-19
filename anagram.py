# Sort strings, then compare them and see if they are anagrams
# We sort them with merge sort alphabetically
def merge_sort(my_string):
    if len(my_string) <= 1:
        return my_string

    sorted = []
    mid = len(my_string) / 2
    left = merge_sort(my_string[:mid])
    right = merge_sort(my_string[mid:])
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted.append(right[right_index])
        right_index += 1

    # Return the sorted sub-array
    return sorted

def is_anagram(string1, string2):
    is_valid_anagram = False
    if merge_sort(string1) == merge_sort(string2):
        is_valid_anagram = True
    return is_valid_anagram

print(is_anagram('loop', 'polo'))
