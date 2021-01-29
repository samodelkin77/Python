def isBalanced(s):
    d = {"(" : 1009, "[" : 1013, "{" : 1019, ")" : -1009, "]" : -1013, "}" : -1019}
    bracketSequence = []
    for b in [d [x] for x in s]:
        l = len (bracketSequence) - 1
        if l == -1:   # closing bracket at the very beginning 
            if b < 0:
                return "NO"
            else:
                bracketSequence.append (b)
        else:
            if bracketSequence [l] % b == 0:
                bracketSequence [l] = bracketSequence [l] + b
                if bracketSequence [l] == 0:
                    l += -1
                    bracketSequence.pop()
            else:
                if b > 0:
                    bracketSequence.append (b)
                    l += 1
                else:
                    return "NO"
    if len (bracketSequence) == 0:
        return "YES"
    else:
        return "NO"


def testCases():
    return [
        ['(', 'NO'],
        [')', 'NO'],
        ['()', 'YES'],
        [')(', 'NO'],
        ['([])', 'YES'],
        ['([)]', 'NO'],
        ['((({})[[]]))', 'YES'],
        ['((({}[[]]))', 'NO'],
        ['{[()]}', 'YES'],
        ['{[(])}', 'NO'],
        ['{{[[(())]]}}', 'YES']
    ]

for t in testCases():    
    r = isBalanced(t[0]) 
    if r != t[1]:
        print ('Wrong', r, t[0])
