
# coding: utf-8

# In[ ]:


COMPUTER = 'X'
USER  = '*'

FUNCTION_CALLS = 0

def prepareBoard(size):
	board = []
	row = []
	for number in range(1, size*size+1):
		row.append(str(number))
		if (number) % size == 0:
			board.append(row)
			row = []
	return board

def printBoard(board):
	for row in board:
		print row
		
def isMoveLeft(board):
	for row in board:
		for element in row:
			if element != COMPUTER and element != USER:
				return True
	return False
	
def evaluate(board):
	global COMPUTER, USER
	size = len(board)
	for row in range(size):
		if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
			if board[row][0] == COMPUTER:
				return 10
			else:
				return -10
	
	for col in range(size):
		if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
			if board[0][col] == COMPUTER:
				return 10
			else:
				return -10
			
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		if board[0][0] == COMPUTER:
			return 10
		else:
			return -10
			
	if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		if board[0][2] == COMPUTER:
			return 10
		else:
			return -10
	return 0

def minmax(board, depth, maximizeScore):
	global COMPUTER, USER, FUNCTION_CALLS

	FUNCTION_CALLS += 1

	size = len(board)
	score = evaluate(board)
	if score == -10 or score == 10:
		return score
	
	if not isMoveLeft(board):
		return 0
	
	if maximizeScore:
		bestScore = -1000
		for row in range(size):
			for col in range(size):
				if board[row][col] != COMPUTER and board[row][col] != USER:
					defaultVal = board[row][col]
					board[row][col] = COMPUTER
					bestScore = max(bestScore, minmax(board, depth + 1, False))
					board[row][col] = defaultVal
					if bestScore > 0:
						return bestScore
		return bestScore
	else:
		worstScore = 1000
		for row in range(size):
			for col in range(size):
				if board[row][col] != COMPUTER and board[row][col] != USER:
					defaultVal = board[row][col]
					board[row][col] = USER
					worstScore = min(worstScore, minmax(board, depth + 1, True))
					board[row][col] = defaultVal
					if worstScore < 0:
						return worstScore
		return worstScore

def placeComputer(board, depth):
	global COMPUTER, USER
	prow, pcol = None, None
	bestScore = -1000
	size = len(board)
	for row in range(size):
		for col in range(size):
			if board[row][col] != COMPUTER and board[row][col] != USER:
				defaultVal = board[row][col]
				board[row][col] = COMPUTER
				newScore = minmax(board, depth + 1, False)
				if newScore > bestScore:
					prow = row
					pcol = col
					bestScore = newScore
				board[row][col] = defaultVal
	return (prow, pcol)

def printWinner(winner):
	print ''
	if winner == 'COMPUTER':
		print "Beta tumse na ho payega. Kheti-baadi karo tum"
	elif winner == 'USER':
		print "Yeh toh kabhi ho hi nahi sakta"
	else:
		print "Match Draw! Mummy ko bolo ko Complan pilaye"
	


# In[ ]:


if __name__ == '__main__':
	global COMPUTER, USER, FUNCTION_CALLS
	size = 3
	board = prepareBoard(size)
	winner = None
	userChance = False
	for i in range(size * size):
		printBoard(board)
		print "\n"
		
		if userChance:
			userChoice = map(int, raw_input("Enter location : ").split(" "))
			row = userChoice[0]
			col = userChoice[1]
			board[row][col] = USER
		else:
			row, col = placeComputer(board, i + 1)
			board[row][col] = COMPUTER
		
		if evaluate(board) != 0:
			winner = "USER" if userChance else "COMPUTER"
			break
			
		userChance = not userChance
		
	printBoard(board)
	printWinner(winner)
	
	print "Total Function Calls : {0}".format(FUNCTION_CALLS)
