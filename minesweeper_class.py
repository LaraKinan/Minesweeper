import random

class minesweepers_board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # initialize board
        self.board = self.init_board()
        self.fill_board()

        self.dug = set()
        self.flagged = set()

    # create a board with self.num_bombs number of bombs and distribute randomly 
    def init_board(self):
        board =[[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            bomb = random.randint(0, self.dim_size**2 - 1)
            row = bomb // self.dim_size
            col = bomb % self.dim_size
            if board[row][col] == '*':
                continue
            
            board[row][col] = '*'
            bombs_planted += 1

        return board
    
    # fill the board with the numbers surrounding the bombs
    def fill_board(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == '*':
                    continue
                self.board[row][col] = self.calc_value_cell(row, col)
    
    # Are row and col in the range defined for board
    def in_range(self, row, col):
        if 0 <= row < self.dim_size and 0 <= col < self.dim_size:
            return True
        return False
    
    # Calculate how many bombs are neighboring to (row, col)
    def calc_value_cell(self, row, col):
        neighbor_bombs = 0
        for neighbor_row in range(row - 1, row + 2):
            for neighbor_col in range(col - 1, col + 2):
                if(self.in_range(neighbor_row, neighbor_col) and self.board[neighbor_row][neighbor_col] == '*'):
                    if neighbor_row == row and neighbor_col == col:
                        continue
                    neighbor_bombs += 1
        return neighbor_bombs
    
    # Dig in (row, col)
    def dig(self, row, col):
        if self.in_range(row, col):
            self.dug.add((row, col))

            if self.board[row][col] == '*':
                return False
            elif self.board[row][col] > 0:
                return True
            
            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if (r, c) in self.dug:
                        continue 
                    self.dig(r, c)

            return True
        return True
    
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        string_rep = ''
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep