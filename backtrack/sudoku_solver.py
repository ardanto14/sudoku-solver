class Sudoku:

    def __init__(self, stre):
        self.sudoku = [[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9]
        self.fixed = [[False]*9,[False]*9,[False]*9,[False]*9,[False]*9,[False]*9,[False]*9,[False]*9,[False]*9]

        xi = 0
        y = 0
        for char in stre:
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

    def is_valid(self):
        for i in range(9):
            if not self.valid_in_row(i):
                return False
            if not self.valid_in_column(i):
                return False
        return True

    def solve(self, x=0, y=0):
        if x > 8:
            return
        elif self.fixed[x][y]:
            if y + 1 > 8:
                self.solve(x+1, 0)
            else:
                self.solve(x, y+1) 
        else:
            for i in range(1, 10):
                print(self)
                self.sudoku[x][y] = i
                if self.valid_in_column(y) and self.valid_in_row(x):
                    print("sini")
                    if y + 1 > 8:
                        self.solve(x+1, 0)
                    else:
                        self.solve(x, y+1)
            self.sudoku[x][y] = -1


    def __str__(self):
        ret = ""
        for row in self.sudoku:
            for value in row:
                if value == -1:
                    ret += "-"
                else:
                    ret += str(value)
                ret += " "
            ret += "\n"

        return ret

if __name__ == "__main__":
    inp = input()
    sudoku = Sudoku(inp)
    print(sudoku)
    sudoku.solve()
    print(sudoku)