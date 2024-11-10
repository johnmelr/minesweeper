from random import randint
import os

def setupGrid(gridSize, numberofMines):

	grid = [['0' for i in range(gridSize)] for i in range(gridSize)] #initalize a an nxn matrix and stores it as the grid
	mines = getMines(gridSize, numberofMines) #calls the function getMines and assigns the returned value into mines containing a list
	
	for [x, y] in mines: #loops through the list and gets an x and y coordinate
		grid[x][y] = "X" #The cell that contains the coordinates x and y is given the value "X" implying that it is a bomb
	
	for r in range(gridSize):
		for c in range(gridSize):
			if grid[r][c] != "X": #If a cell is not a bomb, it calls the function adjacentMines and assigns its value to that cell
				grid[r][c] = str(adjacentMines(r, c, 0))

	return grid

def drawGrid(gridSize, emptyGrid):
	clearScreen()
	print(" ", end = "  ")
	alphabet = "abcdefghijklmniopqrstuvwxyz" #Used to display position of the column.

	for i in range(gridSize):
		print(" ", alphabet[i], end = " ")
		
	print()
	
	for i in range(gridSize):
		if i + 1 <= 9:
			print("   ","----" * gridSize)
			print(i+1, " |" , " | ".join(emptyGrid[i]),"|")
		else:
			print("  ","----" * gridSize)
			print(i+1, "|" , " | ".join(emptyGrid[i]),"|")
	print("  ","----" * gridSize)

def getMines(gridSize,numberofMines):

	i = 0
	while i < numberofMines:
	
		x = randint(0, gridSize - 1) #Selects a random x and y value
		y = randint(0, gridSize - 1)

		if [x, y] in mines:			#if the pair already exists in mines, repeats the loop
			continue				#until there are i number of mines.
		else:
			mines.append([x,y])
			i += 1

	return mines

def adjacentMines(r, c, adjacent_Tile): #function that checks the adjacent cell of a chosen cell if how many mines is within its proximity and returns that value as an integer.
	
	if [r+1, c] in mines:
		adjacent_Tile += 1
	
	if [r+1, c+1] in mines:
		adjacent_Tile += 1
	
	if [r, c+1] in mines:
		adjacent_Tile += 1
	
	if [r-1, c+1] in mines:
		adjacent_Tile += 1
	
	if [r-1, c] in mines:
		adjacent_Tile += 1
	
	if [r-1, c-1] in mines:
		adjacent_Tile += 1
	
	if [r, c-1] in mines:
		adjacent_Tile += 1
	
	if [r+1, c-1] in mines:
		adjacent_Tile += 1

	return adjacent_Tile

def getneighbors(grid, r, c):
    gridSize = len(grid)
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (r + i) < gridSize and -1 < (c + j) < gridSize:
                neighbors.append((r + i, c + j))

    return neighbors

def showcells(grid, emptyGrid, r, c):
    if emptyGrid[r][c] != ' ':
        return

    emptyGrid[r][c] = grid[r][c]

    if grid[r][c] == '0':
        for r, c in getneighbors(grid, r, c):
            showcells(grid, emptyGrid, r, c) #Shows the cell if the neiboring cells are 
            #empty and stops in the next adjacent non empty cell.


def clearScreen():
	try:
		os.system('cls')
	except:
		os.system('clear')

def drawGameSign():
	clearScreen()
	print(" ------------------------------------------------------------------------------------------------")
	print("|                                                                                                 |")
	print("|                                                                                                 |")
	print("|   ███╗   ███╗██╗███╗   ██╗███████╗███████╗██╗    ██╗███████╗███████╗██████╗ ███████╗██████╗     |")
	print("|   ████╗ ████║██║████╗  ██║██╔════╝██╔════╝██║    ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗    |")
	print("|   ██╔████╔██║██║██╔██╗ ██║█████╗  ███████╗██║ █╗ ██║█████╗  █████╗  ██████╔╝█████╗  ██████╔╝    |")
	print("|   ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ╚════██║██║███╗██║██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗    |")
	print("|   ██║ ╚═╝ ██║██║██║ ╚████║███████╗███████║╚███╔███╔╝███████╗███████╗██║     ███████╗██║  ██║    |")
	print("|   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝    |")
	print("|                                                                                                 |")
	print("|                                                                                                 |")
	print(" -------------------------------------------------------------------------------------------------")
	print()
	print()

def drawMenu():
	drawGameSign()
	print("Welcome to Minesweeper (Terminal Version)")
	print()
	print("Choose to start")
	print("[1] New Game")
	print("[2] Load game")
	print("[3] Help")
	print("[4] Exit")

def drawDifficulty():
	drawGameSign()
	print("Choose difficulty")
	print("[1] Easy (8 x 8, 10 mines)")
	print("[2] Medium (12 x 12, 15 mines)")
	print("[3] Hard (16 x 16, 20 mines)")
	print("[4] Back")

def help():
	print("To choose a cell, type in row and column (e.g., 1a) and to flag/unflag a cell, type include an f in the beginning of the input (e.g., f1a). \nFor help, type in 'help' keyword at input. Type in 'exit' to leave the game and 'save' to save the progress of your session")

def saving():

	gridHandle = open("grid.sav",'w')	#Save file for the main grid
	emptyGridHandle = open("emptyGrid.sav",'w')	#Save file for the grid of the state of the game.
	mineHandle = open("mine.sav",'w') #Saves the coordinate of the mines
	for i in range(gridSize):
		for j in range(gridSize):
			if j == gridSize - 1:
				gridHandle.write(grid[i][j] + "\n")
			else:
				gridHandle.write(grid[i][j] + ",")
		
	for i in range(gridSize):
		for j in range(gridSize):
			if j == gridSize - 1:
				emptyGridHandle.write(emptyGrid[i][j] + "\n")
			else:
				emptyGridHandle.write(emptyGrid[i][j] + ",")
	
	for i in range(numberofMines):
		for j in range(2):
			if j == 1:
				mineHandle.write(str(mines[i][j]) + "\n")
			else:
				mineHandle.write(str(mines[i][j]) + ",")

	gridHandle.close()
	emptyGridHandle.close()
	mineHandle.close()
	print("Saved Succesfully")

def loading():
	try:
		grid = []
		emptyGrid = []
		mines = []
		board = []
		#Re-initializes the variables so that the when loading the file, it appends the value in the text file as a list.

		gridHandle = open("grid.sav","r")
		emptyGridHandle = open("emptyGrid.sav",'r')
		mineHandle = open("mine.sav",'r')

		for line in gridHandle:
			data = line[:-1].split(",")
			grid.append(data)
		
		for line in emptyGridHandle:
			data = line[:-1].split(",")
			emptyGrid.append(data)
		
		for line in mineHandle:
			data = line[:-1].split(",")
			x = int(data[0])
			y = int(data[1])
			mines.append([x,y])
		
		gridSize = len(grid)
		numberofMines = len(mines)
		counter = numberofMines
		gridHandle.close()
		emptyGridHandle.close()
		mineHandle.close()
		print(gridSize)
		print(numberofMines)
		print(grid)
		print(emptyGrid)

		for i in range(gridSize):	#initializes the counter for loading of the saved file.
			for j in range(gridSize):
				if emptyGrid[i][j] == 'F':
					counter = counter - 1

		return [gridSize, numberofMines, grid, emptyGrid, mines, counter] 

	except:
		return #returns none when no saved file exist.

def getInput():

	alphabet = "abcdefghijklmniopqrstuvwxyz" #The letters will be used to choose the column.
	userInput = input("Enter cell: ")
	row = '' 
	col = 0
	if userInput.lower() == 'exit': 
		return userInput

	elif userInput.lower() == 'save':
		return userInput

	elif userInput.lower() == 'help':
		return userInput

	elif userInput[0].lower() == 'f':
		flag = userInput[0]
		for i in range(gridSize):
			if userInput[-1] in alphabet[i]:
				col = i + 1 #stores the index of the letter selected

		for s in userInput:
			if s.isnumeric():
				row += s #stores the row number selected by the user.
		return [flag, int(row), col] 
	
	else:
		flag = '' #if the user didn't choose to flag.
		for i in range(gridSize):
			if userInput[-1] in alphabet[i]:
				col = i + 1
		for s in userInput:
			if s.isnumeric():
				row += s

		return [flag, int(row), col]
		#Returns a list containing the information about the flag, row, and column input of the user.
def winning():
	 
	print('8    8               8   8  8          8  8\n' 
		'8    8 eeeee e   e   8   8  8 e  eeeee 88 88\n'
		'8eeee8 8  88 8   8   8e  8  8 8  8   8 88 88\n'
		'  88   8   8 8e  8   88  8  8 8e 8e  8 88 88\n'
  		'  88   8   8 88  8   88  8  8 88 88  8      \n'
  		'  88   8eee8 88ee8   88ee8ee8 88 88  8 88 88\n')
	

def playGame(gridSize,numberofMines, grid, emptyGrid, counter):
	clearScreen()
	drawGrid(gridSize, emptyGrid)
	alphabet = "abcdefghijklmniopqrstuvwxyz"
	help()
	while True:
	
		try:
			print("Mines remaining: ", counter)
			
			try:
				play = getInput()
				choose = play[0]
				row = play[1] - 1
				column = play[2] - 1
				if row > gridSize or column > gridSize or row < 0 or column < 0:
					drawGrid(gridSize, emptyGrid)
					print("The given input should not be lower or higher than " + str(gridSize) + " and should be from " + alphabet[0] + "-" + alphabet[gridSize])
	 
				else: 
					if choose.lower() == 'f':
						if emptyGrid[row][column] == ' ':
							emptyGrid[row][column] = 'F'
							drawGrid(gridSize, emptyGrid)
							counter = counter - 1

						elif emptyGrid[row][column] == 'F':
							emptyGrid[row][column] = ' '
							drawGrid(gridSize, emptyGrid)
							counter = counter + 1

						else:					
							drawGrid(gridSize, emptyGrid)
							print("Can't flag here")


					elif choose.lower() == '' or  choose.lower() == ' ':
						
						if emptyGrid[row][column] == 'F':
							drawGrid(gridSize, emptyGrid)
							print("This cell is flagged")

						elif [row, column] in mines:
							drawGrid(gridSize, grid)
							print("YOU STEPPED ON A MINE! GAME OVER.")
							try:
								input()
								break
							except KeyboardInterrupt:
								break

						elif emptyGrid[row][column] != ' ':
							drawGrid(gridSize, emptyGrid)
							print("The cell is already open")

						elif grid[row][column] == '0':
							showcells(grid,emptyGrid,row,column)
							drawGrid(gridSize, emptyGrid)

						else:
							emptyGrid[row][column] = grid[row][column]
							drawGrid(gridSize, emptyGrid)


			except:
				choose = play
				if choose.lower() == 'help':
					drawGrid(gridSize, emptyGrid)
					help()

				elif choose.lower() == 'save':
					if os.path.exists("mine.sav") and os.path.exists("grid.sav") and os.path.exists("emptyGrid.sav"):
						yesorno = input("Are you sure you want to overwrite saved file? Doing this will remove previous saved game. (Y/N): ")
						if yesorno.lower() == 'y':
							drawGrid(gridSize, emptyGrid)
							saving()
							break

						else:
							drawGrid(gridSize, emptyGrid)
							continue
					
					else:
						drawGrid(gridSize, emptyGrid)
						saving()

				elif choose.lower() == 'exit':
					print("Input any key (except for y) if you wish to continue playing.")
					exit = input("Are you sure you want to exit? (Y/N): ")
					if exit.lower() == 'y':
						break
					else:
						drawGrid(gridSize, emptyGrid)

				else:
					drawGrid(gridSize, emptyGrid)
					print('Invalid input')
					help()
			
		except:

			drawGrid(gridSize, emptyGrid)
			print('Invalid input')
			help()
		
		win = False
			
		for i in range(gridSize):
			for j in range(gridSize):
				if emptyGrid[i][j] != ' ':
					win = True
					continue
				elif emptyGrid[i][j] == ' ':
					if grid[i][j] == 'X':
						win = True
						continue
					else:
						win = False
						break
			if win:
				continue
			else:
				break
		if win:
			winning()
			input("Press enter to continue...")
			break	

drawMenu()

while True:
	
	mines = []
	grid = []
	emptyGrid = []

	try:
		
		choice = int(input("Enter your choice: "))

		if choice == 1:
			if os.path.exists("mine.sav") and os.path.exists("grid.sav") and os.path.exists("emptyGrid.sav"):
				yesorno = input("Are you sure you want to start a new game? Doing this will remove previous saved game. (Y/N): ")
				if yesorno.lower() == 'y':
					os.remove("mine.sav")	#deletes the previous saved file
					os.remove("emptyGrid.sav")
					os.remove("grid.sav")
				else:
					drawMenu()
					continue	
				
			drawDifficulty()

			while True:

				try:

					diffChoice = int(input("Enter your choice: "))
				
					if diffChoice == 1:
						gridSize = 8
						numberofMines = 10
						counter = numberofMines
						emptyGrid = [[' ' for i in range(gridSize)] for i in range(gridSize)]
						grid = setupGrid(gridSize,numberofMines)
						playGame(gridSize,numberofMines, grid, emptyGrid, counter)
						break

					elif diffChoice == 2:
						gridSize = 12
						numberofMines = 15
						counter = numberofMines
						emptyGrid = [[' ' for i in range(gridSize)] for i in range(gridSize)]
						grid = setupGrid(gridSize,numberofMines)
						playGame(gridSize, numberofMines, grid, emptyGrid, counter)
						break

					elif diffChoice == 3:
						gridSize = 16
						numberofMines = 20
						counter = numberofMines
						emptyGrid = [[' ' for i in range(gridSize)] for i in range(gridSize)]
						grid = setupGrid(gridSize,numberofMines)
						playGame(gridSize, numberofMines, grid, emptyGrid,counter)
						break

					elif diffChoice == 4:
						break
					
					else:
						drawDifficulty()
						print("Invalid Input")

				except:
					drawDifficulty()
					print("Invalid Input")
			drawMenu()
			
		elif choice == 2:
			board = loading() #stores the returned value of the function loading()

			if board != None:
				gridSize = board[0] #Since the value of board is a list, the first element of it contains the size of the board
				numberofMines = board[1] #The second element contains the value of the number of mines
				grid = board[2] #The third element contains the main grid of the game
				emptyGrid = board[3] #The 4th element contains the grid state of the game 
				mines = board[4] #Stores the coordinate pair of the mines
				counter = board[5] #The counter dictates the amount of mines left unfound in the board
				playGame(gridSize,numberofMines, grid, emptyGrid, counter)
			
			else:
				drawMenu()
				print("No saved game found.")
				try:
					input()
				except:
					drawMenu()

		elif choice == 3:
			clearScreen()
			drawGameSign()
			print("Uncover the empty squares, while avoiding the times. You win if you uncover all the safe squares and you lose if you trigger a mine.")
			input("Press enter to go back.")

		elif choice == 4:
			break

		else:
			drawMenu()
			print("Invalid input")
		
		drawMenu()

	except:
		drawMenu()
		print("Invalid input")

