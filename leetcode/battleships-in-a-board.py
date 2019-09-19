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
                    # print (max(0,i-1), min(wboard-1,i+1)-1, max(0,i-1), min(wboard,i+1)-1)
                    for x in (max(0,i-1), min(wboard-1,i+1)):
                        for y in (max(0,j-1), min(hboard-1,j+1)):
                            if x != i and y != j:
                                print ('x=%i, y=%i, board[x][j]=%s' % (x, y, board [x][y]))
                                if board [x][j] == 'X' or board [i][y]:
                                    xcount =+ 1
                    if xcount == 0:
                        print ('Evrika!!! i=%i j=%i xcount=%i' % (i, j, xcount))
                        result += 1
                    else:
                        print ('Xyevrika!!! i=%i j=%i xcount=%i' % (i, j, xcount))
                        result += 0.5
                    
        return result
                # print (board [i][j])

z = Solution()
b = [
        ['.','X','.','.'],
        ['.','.','.','X'],
        ['.','.','.','X'],
        ['X','X','.','.'],
    ]
print (z.countBattleships(b))
