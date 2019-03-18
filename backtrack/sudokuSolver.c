#include <stdio.h>
#include <stdbool.h>

int sudoku[9][9];
bool cant_delete[9][9];
    
void insertAnswer(int x, int y, int value) {
    if (!cant_delete[x][y]) {
        sudoku[x][y] = value;
    }
}

bool validInRow(int x) {
    int registered[9];
    int numberOfRegistered = 0;
    
    for (int i = 0; i < 9; i++) {
        if (sudoku[x][i] == -1) {
            continue;
        }
        
        // search if number is registered
        for (int j = 0; j < numberOfRegistered; j++) {
            if (sudoku[x][i] == registered[j]) {
                return false;
            }
        }
        
        // if not then store to registered
        registered[numberOfRegistered] = sudoku[x][i];
        numberOfRegistered++;
    }
    
    return true;
}

bool validInColumn(int y) {
    int registered[9];
    int numberOfRegistered = 0;
    
    for (int i = 0; i < 9; i++) {
        if (sudoku[i][y] == -1) {
            continue;
        }
        
        // search if number is registered
        for (int j = 0; j < numberOfRegistered; j++) {
            if (sudoku[i][y] == registered[j]) {
                return false;
            }
        }
        
        // if not then store to registered
        registered[numberOfRegistered] = sudoku[i][y];
        numberOfRegistered++;
    }
    
    return true;
}

bool validInArea(int x, int y) {
    int lower_x = x;
    int upper_x = x;
    int lower_y = y;
    int upper_y = y;
    
    // set boundary
    while (true) {
        int num_valid = 0;
        if (lower_x % 3 == 0) {
            num_valid++;
        } else {
            lower_x--;
        }
        
        if ((upper_x + 1) % 3 == 0) {
            num_valid++;
        } else {
            upper_x++;
        }
        
        if (lower_y % 3 == 0) {
            num_valid++;
        } else {
            lower_y--;
        }
        
        if ((upper_y + 1) % 3 == 0) {
            num_valid++;
        } else {
            upper_y++;
        }
        
        if (num_valid == 4) {
            break;
        }
    }
    
    int registered[9];
    int numberOfRegistered = 0;
    for (int i = lower_x; i <= upper_x; i++) {
        for (int j = lower_y; j <= upper_y; j++) {
            if (sudoku[i][j] == -1) {
                continue;
            }
            
            for (int k = 0; k < numberOfRegistered; k++) {
                if (registered[k] == sudoku[i][j]) {
                    return false;
                }
            }
            
            registered[numberOfRegistered] = sudoku[i][j];
            numberOfRegistered++;
        }
    }
    return true;
}

void printSudoku() {
    for (int i = 0; i < 9; i++) {
        if (i % 3 == 0 && i != 0) {
            printf("---------------------\n");
        }
        for (int j = 0; j < 9; j++) {
            if (j % 3 == 0 && j != 0) {
                printf("| ");
            }
            
            if (sudoku[i][j] == -1) {
                printf("-");
            } else {
                printf("%d", sudoku[i][j]);
            }
            printf(" ");;
        }
        printf("\n");
    }
    printf("\n\n");
}

bool solve(int x, int y) {
    if (x > 8) {
        return true; 
    } else if (cant_delete[x][y]) {
        if (y + 1 > 8) {
            return solve(x+1, 0);
        } else {
            return solve(x, y+1);
        }
    } else {
        bool retval = false;
        for (int i = 1; i < 10; i++) {
            sudoku[x][y] = i;
            if (validInColumn(y) && validInRow(x) && validInArea(x, y)) {
                if (y + 1 > 8) {
                    retval = solve(x+1, 0);
                } else {
                    retval = solve(x, y+1);
                }
            }
            if (retval) {
                return true;
            }
        }
        
        sudoku[x][y] = -1;
        return false;
        
    }
}

int main() {
    // set default
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cant_delete[i][j] = false;
        }
    }

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            sudoku[i][j] = -1;
        }
    }
    
    // read input and store to array
    FILE *fp;
    char achar;
    fp = fopen("input.txt", "r");
    int x = 0;
    int y = 0;
    for (int i = 0; i < 90; i++) {
        achar = fgetc(fp);
        if (achar == '=') {
            x++;
            y = 0;
            continue;
        }
        
        if (achar == '-') {
            sudoku[x][y] = -1;
            cant_delete[x][y] = false;
        } else {
            sudoku[x][y] = ((int) achar) - 48;
            cant_delete[x][y] = true;
        }
        y++;
    }
    
    // print before solving
    printSudoku();
    
    solve(0, 0);
    
    // print after solving
    printSudoku();
    
    return 0;   
}
