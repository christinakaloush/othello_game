class Othello(object):
    """Othello class implements the game logic of the Othello board game."""

    # Useful constants - access these class attributes using format "classname.attributename"
    BLACK = 'B'     # access as Othello.BLACK
    WHITE = 'W'     # access as Othello.WHITE
    EMPTY = 'E'     # access as Othello.EMPTY
    PLAYER1 = 1     # access as Othello.PLAYER1
    PLAYER2 = 2     # access as Othello.PLAYER2
    TIE = 0         # access as Othello.TIE

    def __init__(self, board_size, start_player, start_player_disc):
        """
        Iniitializes Othello object's attributes as described below.

        Parameters:
            board_size: size of othello board
            start_player: player that starts the game
            start_player_disc: disc color of the start player

        Instance Attributes:
            self._size (int): initialized with the value of parameter board_size
            self._turn (int): initialized with the value of parameter start_player
            self._player1_disc (str): initialize it appropriately using the value of parameter start_player_disc
            self._player2_disc (str): initialize it appropriately using the value of parameter start_player_disc
            self._board (list of lists): game board initialized appropriately

        Validations and Exceptions:
            Raise ValueError if parameter board_size is not 4 or 6 or 8
            Raise ValueError if parameter start_player is < 1 or > 2
            Raise ValueError if parameter start_player_disc is not valid.
        """
        if board_size < 4 or board_size > 8 or board_size % 2 != 0:
            raise ValueError("Board size can only be 4 or 6 or 8.")
        if start_player < Othello.PLAYER1 or start_player > Othello.PLAYER2:
            raise ValueError("Player number is not valid.")
        if not (start_player_disc == Othello.BLACK or start_player_disc == Othello.WHITE):
            raise ValueError("Disc color is not valid.")

        self._size = board_size
        self._turn = start_player
        
        if start_player == Othello.PLAYER1:
            self._player1_disc = start_player_disc
            self._player2_disc = Othello.WHITE if start_player_disc == Othello.BLACK else Othello.BLACK
        else:
            self._player2_disc = start_player_disc
            self._player1_disc = Othello.WHITE if start_player_disc == Othello.BLACK else Othello.BLACK

        self._board = []

        # Setup the board to initial game board configuration
        for i in range(self._size):
            self._board.append([Othello.EMPTY] * self._size)
        pos = (self._size - 2) // 2
        self._board[pos][pos] = Othello.BLACK
        self._board[pos][pos+1] = Othello.WHITE
        self._board[pos+1][pos] = Othello.WHITE
        self._board[pos+1][pos+1] = Othello.BLACK


    def get_board_size(self):
        """Returns the board size."""
        return self._size


    def get_turn(self):
        """Returns the current value of self._turn indicating whose turn it is currently."""
        return self._turn


    def set_next_turn(self):
        """Sets the value of self._turn to next player."""
        if self._turn == Othello.PLAYER1:
            self._turn = Othello.PLAYER2
        else:
            self._turn = Othello.PLAYER1

    def get_player_disc(self, player):
        """
        Return the disc of player indicated by parameter player.

        Parameter:
            player (int): player number whose disc is returned

        Validations and Exceptions:
            Raise ValueError if parameter player is < 1 or > 2
        """
        if player == 1:
            return self._player1_disc
        elif player == 2:
            return self._player2_disc
        else:
            raise ValueError("Invalid number, must be 1 or 2")

    def is_valid_move(self, row, col, disc):
        """
        Return True if placing the disc at location row,col is valid; False otherwise.

        Parameters:
            row (int): row number (0-based index)
            col (int): column number (0-based index)
            disc (str): disc color
       
        Validations and Exceptions:
            Return False if row and/or col values is not within the bounds of the board.
            Raises ValueError if the value of parameter disc is not valid.
        """
        
        #Check if it is a valid disc
        if not (disc == Othello.BLACK or disc == Othello.WHITE):
            raise ValueError("Disc color is not valid.")
        
        #Check if row and col values are within bounds of the board
        if row < 0 or row >= self._size or col < 0 or col >= self._size:
            return False
        
        #Check if cell at row, col is occupied
        if self._board[row][col] != Othello.EMPTY:
            return False
        
        opponent_disc = Othello.WHITE if disc == Othello.BLACK else Othello.BLACK
        
        #Check for horizontal match to the left (West)
        r = row
        c = col - 1
        while c >= 0 and self._board[r][c] == opponent_disc:
            c -= 1
        if (c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):
            return True
        
        #Check for horizontal match to the right (East)
        r = row
        c = col + 1
        while c < self._size and self._board[r][c] == opponent_disc:
            c += 1
        if (c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):
            return True
        
        #Check for vertical match up top (North)
        r = row - 1
        c = col
        while r >= 0 and self._board[r][c] == opponent_disc:
            r -= 1
        if (r >= 0 and r < self._size and abs(r - row) > 1 and self._board[r][c] == disc):
            return True
        
        #Check for vertical match down below (South)
        r = row + 1
        c = col
        while r < self._size and self._board[r][c] == opponent_disc:
            r += 1
        if (r >= row and r < self._size and abs(r - row) > 1 and self._board[r][c] == disc):
            return True      
        
        #Check for diagonal match above and to the right (Northeast)
        r = row - 1
        c = col + 1
        while c < self._size and r >= 0 and self._board[r][c] == opponent_disc:
            r -= 1
            c += 1
        if (r >= 0 and r < self._size and abs(r - row) > 1 and c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):        
            return True
            
        #Check for diagonal match above and to the left (Northwest)
        r = row - 1
        c = col - 1
        while c >= 0 and r >= 0 and self._board[r][c] == opponent_disc:
            r -= 1
            c -= 1
        if (r >= 0 and r < self._size and abs(r - row) > 1 and c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):        
            return True
            
        #Check for diagonal match below and to the left (Southwest)
        r = row + 1
        c = col - 1
        while c >= 0 and r < self._size and self._board[r][c] == opponent_disc:
            r += 1
            c -= 1
        if (r >= 0 and r < self._size and abs(r - row) > 1 and c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):        
            return True
        
        #Check for diagonal match below and to the right (Southeast)
        r = row + 1
        c = col + 1
        while c < self._size and r < self._size and self._board[r][c] == opponent_disc:
            r += 1
            c += 1
        if (r >= 0 and r < self._size and abs(r - row) > 1 and c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):        
            return True
        
        return False
    
    def is_a_valid_move_available(self, disc):
        """
        Return True if a valid move for disc is available; False otherwise.

        Parameter:
            disc (str): disc color
        """
        #Check if a valid move is available
        for i in range(self._size):
            for j in range(self._size):
                if self.is_valid_move(i,j,disc):
                    return True
        return False


    def place_disc_at_pos(self, row, col, disc):
        """
        Place the disc at location row,col on the board, if valid.

        Parameters:
            row (int): row number (0-index based)
            col (int): column number (0-index based)
            disc (str): disc color
       
        Validations and Exceptions:
            Return None if placement of disc at location row,col is not valid (use is_valid_move() to check this).
        """ 

        if not self.is_valid_move(row, col, disc):
            return None
        
        opponent_disc = Othello.WHITE if disc == Othello.BLACK else Othello.BLACK
        
        #Place discs at horizontal matches to the left (West)
        r = row
        c = col - 1
        while c >= 0 and self._board[r][c] == opponent_disc:
            c -= 1
        if (c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):
            for i in range(abs(c - col)):
                self._board[row][col - i] = disc
                
        #Place discs at horizontal matches to the right (East)
        r = row
        c = col + 1
        while c < self._size and self._board[r][c] == opponent_disc:
            c += 1 
        if (c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):
            for i in range(abs(c - col)):
                self._board[row][col + i] = disc
        
        #Place discs at vertical matches up top (North)
        r = row - 1
        c = col
        while r >= 0 and self._board[r][c] == opponent_disc:
            r -= 1
        if (r >= 0 and r < self._size and abs(r - row) > 1 and self._board[r][c] == disc):
            for i in range(abs(r - row)):
                self._board[row - i][col] = disc
        
        #Place discs at vertical matches down below (South)
        r = row + 1
        c = col
        while r < self._size and self._board[r][c] == opponent_disc:
            r += 1
        if (r >= 0 and r < self._size and abs(r - row) > 1 and self._board[r][c] == disc):
            for i in range(abs(r - row)):
                self._board[row + i][col] = disc
        
        #Place discs at diagonal matches above and to the right (Northeast)
        r = row - 1
        c = col + 1
        while c < self._size and r >= 0 and self._board[r][c] == opponent_disc:            
            r -= 1
            c += 1
        while r >= 0 and c < self._size and abs(r - row) > 1 and abs(c - col) > 1 and self._board[r][c] == disc:       
            self._board[row][col] = disc
            self._board[r + 1][c - 1] = disc
            c -= 1
            r += 1
            
        #Place discs at diagonal matches above and to the left (Northwest)
        r = row - 1
        c = col - 1
        while c >= 0 and r >= 0 and self._board[r][c] == opponent_disc:
            r -= 1
            c -= 1
        while (r >= 0 and r < self._size and abs(r - row) > 1 and c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):        
            self._board[row][col] = disc
            self._board[r + 1][c + 1] = disc
            c += 1
            r += 1
            
        #Place discs at diagonal matches below and to the left (Southwest)
        r = row + 1
        c = col - 1
        while c >= 0 and r < self._size and self._board[r][c] == opponent_disc:            
            r += 1
            c -= 1
        while c >= 0 and r < self._size and abs(r - row) > 1 and abs(c - col) > 1 and self._board[r][c] == disc:       
            self._board[row][col] = disc
            self._board[r - 1][c + 1] = disc
            c += 1
            r -= 1
            
        #Place discs at diagonal matches below and to the right (Southeast)
        r = row + 1
        c = col + 1
        while c < self._size and r < self._size and self._board[r][c] == opponent_disc:
            r += 1
            c += 1
        while (r >= 0 and r < self._size and abs(r - row) > 1 and c >= 0 and c < self._size and abs(c - col) > 1 and self._board[r][c] == disc):        
            self._board[row][col] = disc
            self._board[r - 1][c - 1] = disc
            c -= 1
            r -= 1
                   
        if not self.is_game_over():
            self.set_next_turn()

    def is_board_full(self):
        """Returns True if the board is full; False otherwise."""
        empty_counter = 0
        for i in range(self._size):
            for j in range(self._size):
                if self._board[i][j] != Othello.EMPTY:
                    empty_counter += 1
        if empty_counter == self._size * self._size:
            return True
        else:
            return False
        
    def is_game_over(self):
        """Returns True if the game is over; False otherwise."""
        if not self.is_a_valid_move_available(Othello.WHITE) and \
            not self.is_a_valid_move_available(Othello.BLACK):
                return True
        elif self.is_board_full():
            return True
        else:
            return False
        
    def who_won(self):
        """
        If game is over, return the player number that won the game. In case of a tie, return
        Othello.TIE. Return None if game is not over.
        """
        if not self.is_game_over():
            return None
        
        if self.is_game_over():
            return self.get_turn()
        else:
            return Othello.TIE
        
    def __repr__(self):
        """Returns printable representation of Othello object."""
        result_str = "\n  "
        for i in range(self._size):
            result_str += str(i) + " "
        result_str = result_str.rstrip() + "\n"
        for i in range(self._size):
            result_str += str(i) + " "
            for j in range(self._size):
                if self._board[i][j] == Othello.WHITE:
                    result_str += "W "
                elif self._board[i][j] == Othello.BLACK:
                    result_str += "B "
                else:
                    result_str += "- "
            result_str = result_str.rstrip() + "\n"  
        return result_str 

