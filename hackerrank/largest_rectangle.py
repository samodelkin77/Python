#largest_rectangle

def largestRectangle(h):
    l = len (h) 
    if l == 1:
        return h[0]
    elif l == 2:
        return 2 * min ([h[0], h[1]])
    min_l = [-1]
    stack = [0]
    for i in range (1, l):
        while len (stack) > 0 and h [i] <= h [stack [-1]]:
            stack.pop()
        if len (stack) == 0:
            min_l.append (-1)
        else:
            min_l.append (stack [-1])
        stack.append (i)

    min_r = [0] * (l - 1)
    min_r.append (l)
    stack = [l - 1]
    for i in range (l - 2, -1, -1):
        while len (stack) > 0 and h [i] <= h [stack [-1]]:
            stack.pop()
        if len (stack) == 0:
            min_r [i] = l
        else:
            min_r [i] =  stack [-1]
        stack.append (i)

    # for i in range (l):
    #     print (i, h [i], max_l [i], max_r [i])
    m = 0
    for i in range (l):
        s = (min_r [i] - min_l [i] - 1) * h [i] 
        # print (i, min_r [i], s)
        if s > m:
            m = s

    return m

        



# print (largestRectangle ([11, 11, 10, 10, 10]))
print (largestRectangle ([1, 2, 3, 4, 5]))