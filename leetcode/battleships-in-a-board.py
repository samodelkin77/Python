class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        wboard, hboard = len (board), len (board[0])
        
        for i in range (wboard):
            for j in range (hboard):
                if board [i][j] == 'X':
                    print ('i=%i, j=%i, board[i][j]=%s' % (i, j, board [i][j]))
                    xcount = 0
                    for c in list (filter (lambda x: x[0] in range (wboard) and x[1] in range (hboard), [[i+x,j+y] for x in [1,-1] for y in [1, -1]])):
                        print ('c=', c, board [c[0]][c[1]])
                        if board [c[0]][c[1]] == 'X':
                            xcount += 1
                    if xcount == 0:
                        print ('Evrika!!! i=%i j=%i xcount=%i' % (i, j, xcount))
                        result += 1
                    elif xcount == 1:
                        print ('Xyevrika!!! i=%i j=%i xcount=%i' % (i, j, xcount))
                        result += 0.5
                    
        return int(result)
                # print (board [i][j])

z = Solution()
b = [
        ['.','X','.','.'],
        ['.','.','.','X'],
        ['.','.','.','X'],
        ['X','X','.','.'],
    ]
# b = [
#     ["X",".",".","X"],
#     [".",".",".","X"],
#     [".",".",".","X"]
# ]
# b = [["X","X","X"]]
print (z.countBattleships(b))

# i, j, wboard, hboard = 1, 3, 3, 4
# for x in list (filter (lambda z: z >= 0 and z < wboard, [i-1, i+1])):
#     print (x)
#     for y in list (filter (lambda z: z >= 0 and z < hboard, [j-1, j+1])):
#         print (y, b [x][j], b [i][y])
        