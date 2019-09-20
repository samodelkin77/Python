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
                    # print ('i=%i, j=%i, board[i][j]=%s' % (i, j, board [i][j]))
                    if (i >= wboard-1 or board [i+1][j] == '.') and (j >= hboard - 1 or board [i][j+1] == '.'):
                        result += 1
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
        