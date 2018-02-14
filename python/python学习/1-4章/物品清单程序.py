theBoard = {1 : ' ',2 : ' ',3 : ' ',
			4 : ' ',5 : ' ',6 : ' ',
			7 : ' ',8 : ' ',9 : ' '}
def printBoard(board):
	print(board[1] + '|' + board[2] + '|' + board[3] )
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6] )
	print('-+-+-')
	print(board[7] + '|' + board[8] + '|' + board[9] )
def checkWin(broad,letter):
    if ((broad[1] ==letter and broad[2] == letter and broad[3] ==letter )
    or (broad[4] ==letter and broad[5] ==letter and broad[6] ==letter )
    or (broad[7] ==letter and broad[8] ==letter and broad[9] ==letter )
    
    or (broad[1] ==letter and broad[4] ==letter and broad[7] ==letter )
    or (broad[2] ==letter and broad[5] ==letter and broad[8] ==letter )
    or (broad[3] ==letter and broad[6] ==letter and broad[9] ==letter )
    
    or (broad[7] ==letter and broad[5] ==letter and broad[3] ==letter )
    or (broad[1] ==letter and broad[5] ==letter and broad[9] ==letter )
    ):
        return True
    else :
    	return False

turn = 'X'
printBoard(theBoard)
for i in range(9):
	print("Turn for " + turn + '. Move on which space?')
	move = input()
	theBoard[int(move)] = turn#输入的字符转换为数字
	printBoard(theBoard) 
	if checkWin(theBoard,turn ):
		print(turn + " 方胜 ")
		break                                 
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
	