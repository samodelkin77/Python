#min-max-riddle

def riddle(arr):
    arr_length = len (arr)
    result = [0]
    mins = []
    for n in arr:
        mins.append (n)
        if n > result [0]:
            result [0] = n
    for l in range (1, arr_length):
        result.append (0)
        print (mins [:arr_length - l])
        for i in range (arr_length - l):
            m = min (mins [i], mins [i + 1])
            if m > result [l]:
                result [l] = m
            mins [i] = m
    return result


print (riddle ([1, 2, 3, 5, 1, 13, 3]))
