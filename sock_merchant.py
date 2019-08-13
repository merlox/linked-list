def sock_merchant(n, arr):
    matching_pairs = 0
    restart = True
    index = 0
    while restart:
        increase_index = True
        for sock_two in arr[(index+1):]:
            if arr[index] == sock_two:
                matching_pairs += 1
                del arr[index]
                del arr[arr.index(sock_two)]
                increase_index = False
                break
        if increase_index: index += 1
        if index >= len(arr):
            restart = False
    return matching_pairs
