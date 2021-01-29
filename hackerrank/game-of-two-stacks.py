ef twoStacks(x, a, b):
    s, sum_b = 0, []
    for i, v in enumerate (b):
        s += v
        if s > x:
            break
        sum_b.append (s)

    if len(a) == 0:
        return len (sum_b)
    result, s = len (sum_b), 0
    ib = len (sum_b) - 1
    # print (sum_b)
    for i, v in enumerate (a):
        s += v
        if s > x:
            break
        while ib >= 0 and s + sum_b [ib] > x:
            ib -= 1
        if i + ib + 2 > result:
            # print ('Result ', a[:i + 1], b [:ib + 1])
            result = i + 1 + ib + 1
    return result

        
testCases = [
        [4, 10, [4,2,4,6,1], [2, 1, 8, 5]],
        [3, 10, [4,2,4,6,1], []],
        [3, 4, [0,4,2,4,6,1], [0]],
        [2, 4, [0,4,2,4,6,1], []],
        [2, 4, [], [0,4,2,4,6,1]],
        [1, 4, [5], [0]],
        [0, 3, [5], [4]]
    ]


for tc in testCases:
    r =  twoStacks (tc [1], tc [2], tc [3])
    if r != tc [0]:
        print ('Failed', tc, r)