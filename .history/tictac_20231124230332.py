import math
board = {1: ' ', 2:' ' ,3:' ',
        4: ' ', 5:' ',6:' ',
        7: ' ', 8:' ',9:' '

}
def printBoard(board):
    print(board[1]+ '|' + board[2] + '|'+board[3])
    print('-+-+-')
    print(board[4]+ '|' + board[5] + '|'+board[6])
    print('-+-+-')
    print(board[7]+ '|' + board[8] + '|'+board[9])
    print('-+-+-')




    # A simple Python3 program to find
# maximum score that
# maximizing player can get


def minimax (curDepth, nodeIndex,
			maxTurn, scores, 
			targetDepth):

	# base case : targetDepth reached
	if (curDepth == targetDepth): 
		return scores[nodeIndex]
	
	if (maxTurn):
		return max(minimax(curDepth + 1, nodeIndex * 2, 
					False, scores, targetDepth), 
				minimax(curDepth + 1, nodeIndex * 2 + 1, 
					False, scores, targetDepth))
	
	else:
		return min(minimax(curDepth + 1, nodeIndex * 2, 
					True, scores, targetDepth), 
				minimax(curDepth + 1, nodeIndex * 2 + 1, 
					True, scores, targetDepth))
	
# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))

# This code is contributed
# by rootshadow
