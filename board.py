# coding: utf-8
# Game board. It needs a height and a width in order
# to be instantiated
class board:
    def __init__(self, height, width):
        # Set the height and width of the game board
        self.width = width
        self.height = height
        # Create two lists which will contain the pieces each player posesses
        self.blacklist = []
        self.whitelist = []
        # Set default piece positions
        for i in range(width):
            self.blacklist.append((i, (i+1)%2))
            self.whitelist.append((i, height - (i%2) - 1))
        # boardState contains the current state of the board for printing/eval
        self.boardState = [[' '] * self.width for x in range(self.height)]
        self.gameWon = False
        self.turn = 0 # 0 = white, 1 = black
    
    # Returns True if there is a piece at that position 
    def contains(self, x, y):
        if ((x,y) in self.blacklist):
            # testing return "Black piece is at " + str(x) +","+ str(y)
            return True
        elif ((x,y) in self.whitelist):
            # testing return "White piece is at " + str(x) +","+ str(y)
            return True
        else:
            # testing return "No piece at " + str(x) +","+ str(y)
            return False
    
    # Generate ALL OF THE MOVES
    def iterWhiteMoves(self):
        for piece in self.whitelist:
            for move in self.iterWhitePiece(piece):
                yield move
                
    def iterBlackMoves(self):
        for piece in self.blacklist:
            for move in self.iterBlackPiece(piece):
                yield move
        
    # Creates an iterable list of moves for a white piece
    def iterWhitePiece(self, piece):
        # White pieces can only move up the board
        possibleMove1 = (piece[0]+1, piece[1]-1)
        possibleMove2 = (piece[0]-1, piece[1]-1)
        for move in (possibleMove1, possibleMove2):
            # The move must not go outside the bounds of the board or move to 
            # a location where another piece is already located
            if ((move[0] > -1 and move[0] < self.width) 
            and (move[1] > -1 and move[1] < self.height)
            and not(self.contains(piece[0], piece[1]))): # TODO fix for jumping
                yield move
    
    # Creates an iterable list of moves for a black piece
    def iterBlackPiece(self, piece):
        # White pieces can only move up the board
        possibleMove1 = (piece[0]+1, piece[1]+1)
        possibleMove2 = (piece[0]-1, piece[1]+1)
        for move in (possibleMove1, possibleMove2):
            if ((move[0] > -1 and move[0] < self.width)
            and (move[1] > -1 and move[1] < self.height)
            and not(self.contains(piece[0], piece[1]))): # TODO fix for jumping
                yield move
    
    # Updates the array containing the board to reflect the current state
    # of the pieces on the board
    def updateBoard(self):
        for i in range(self.width):
            for j in range(self.height):
                self.boardState[i][j] = " "
        for piece in self.blacklist:
            self.boardState[piece[1]][piece[0]] = u'◆'
        for piece in self.whitelist:
            self.boardState[piece[1]][piece[0]] = u'◇'
        self.turn = self.turn + 1  

    # Move a blackPiece from one spot to another
    def moveBlackPiece(self, piece, move): 
        #TODO add better limits to bad move checking
        if ((move[0] > -1 and move[0] < self.width)
            and (move[1] > -1 and move[1] < self.height)
            and not(self.contains(move[0], move[1]))):
                self.blacklist[self.blacklist.index(piece)] = move
                self.printBoard()
        else:
            print("Not a valid move dickweed!")
        
    def moveWhitePiece(self, piece, move):
        #TODO add better limits to bad move checking
        if ((move[0] > -1 and move[0] < self.width)
            and (move[1] > -1 and move[1] < self.height)
            and not(self.contains(move[0], move[1]))):
                self.whitelist[self.whitelist.index(piece)] = move
                self.printBoard()
        else:
            print("Not a valid move dickweed!")
            
    def printBoard(self):
        print unicode(self)
        
    def __unicode__(self):
        lines = []
        # This prints the numbers at the top of the Game Board
        lines.append('    ' + '   '.join(map(str, range(self.width))))
        # Prints the top of the gameboard in unicode
        lines.append(u'  ╭' + (u'───┬' * (self.width-1)) + u'───╮')
        
        # Updates Game board
        self.updateBoard()
        
        # Print the boards rows
        for num, row in enumerate(self.boardState[:-1]):
            lines.append(chr(num+65) + u' │ ' + u' │ '.join(row) + u' │')
            lines.append(u'  ├' + (u'───┼' * (self.width-1)) + u'───┤')
        
        #Print the last row
        lines.append(chr(self.height+64) + u' │ ' + u' │ '.join(self.boardState[-1]) + u' │')

        # Prints the final line in the board
        lines.append(u'  ╰' + (u'───┴' * (self.width-1)) + u'───╯')
        return '\n'.join(lines)


#    def print_blank(self):
#        print blankboard(self)

## FOR BLANK BOARD ONLY
#    def __blankboard__(self):
#        lines = []
#        # This prints the numbers at the top of the Game Board
#        lines.append('    ' + '   '.join(map(str, range(self.width))))
#        # Prints the top of the gameboard in unicode
#        lines.append(u'  ╭' + (u'───┬' * (self.width-1)) + u'───╮')

#        # Print the boards rows
#        for num in range(self.height-1):
#            lines.append(str(num) + u' │  ' + (u' │  ' * (self.width-1)) + u' │')
#            lines.append(u'  ├' + (u'───┼' * (self.width-1)) + u'───┤')
#        
#        #Print the last row
#        lines.append(str(self.height) + u' │  ' + (u' │  ' * (self.width-1)) + u' │')

#        # Prints the final line in the board
#        lines.append(u'  ╰' + (u'───┴' * (self.width-1)) + u'───╯')
#        return '\n'.join(lines)
