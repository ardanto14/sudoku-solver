class Sudoku:

    def __init__(self, stre):
        self.sudoku = [[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9]
        self.fixed = [[False]*9,[False]*9,[False]*9,[False]*9,[False]*9,[False]*9,[False]*9,[False]*9,[False]*9]
        
        xi = 0
        y = 0
        for char in stre:
            if xi > 8:
                break
            if char == "=":
                xi = xi + 1
                y = 0
                continue

            if char == "-":
                self.sudoku[xi][y] = -1
                self.fixed[xi][y] = False

            else:
                self.sudoku[xi][y] = int(char)
                self.fixed[xi][y] = True
            y += 1

    def insert_answer(self, x, y, value):
        if not self.fixed[x][y]:
            self.sudoku[x][y] = value

    def valid_in_row(self, x):
        registered = []
        for i in range(9):
            if self.sudoku[x][i] == -1:
                continue

            if self.sudoku[x][i] not in registered:
                registered.append(self.sudoku[x][i])
            else:
                return False

        return True

    def valid_in_column(self, y):
        registered = []
        for i in range(9):
            if self.sudoku[i][y] == -1:
                continue

            if self.sudoku[i][y] not in registered:
                registered.append(self.sudoku[i][y])
            else:
                return False

        return True
        
    def valid_in_area(self, x, y):
        lower_x = x
        upper_x = x
        lower_y = y
        upper_y = y
        
        while True:
            num_valid = 0
            if lower_x % 3 == 0:
                num_valid += 1
            else:
                lower_x -= 1
            
            if (upper_x + 1) % 3 == 0:
                num_valid += 1
            else:
                upper_x += 1
            
            if lower_y % 3 == 0:
                num_valid += 1
            else:
                lower_y -= 1
            
            if (upper_y + 1) % 3 == 0:
                num_valid += 1
            else:
                upper_y += 1
                
            if num_valid == 4:
                break
            
        registered = []
        
        for i in range(lower_x, upper_x + 1):
            for j in range(lower_y, upper_y + 1):
                if self.sudoku[i][j] == -1:
                    continue
                    
                if self.sudoku[i][j] not in registered:
                    registered.append(self.sudoku[i][j])
                else:
                    return False
                    
        return True

    def solve(self, x=0, y=0):
        if x > 8:
            return True;
        elif self.fixed[x][y]:
            if y + 1 > 8:
                return self.solve(x+1, 0)
            else:
                return self.solve(x, y+1) 
        else:
            retval = False;
            for i in range(1, 10):
                self.sudoku[x][y] = i
                if self.valid_in_column(y) and self.valid_in_row(x) and self.valid_in_area(x, y):
                    if y + 1 > 8:
                        retval = self.solve(x+1, 0)
                    else:
                        retval = self.solve(x, y+1)
                
                if retval:
                    return True
                    
            self.sudoku[x][y] = -1
            return False


    def __str__(self):
        ret = ""
        for i in range(0, 9):
            if i % 3 == 0 and i != 0:
                ret += "---------------------\n"
            for j in range(0, 9):
                if j % 3 == 0 and j != 0:
                    ret += "| "
                
                if self.sudoku[i][j] == -1:
                    ret += "-";
                else:
                    ret += str(self.sudoku[i][j])
                ret += " "
            ret += "\n"
        ret += "\n\n"

        return ret

if __name__ == "__main__":
    inp = open('input.txt', 'r').read()
    sudoku = Sudoku(inp)
    print(sudoku)
    sudoku.solve()
    print(sudoku)
