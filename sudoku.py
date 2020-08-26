import sys
sys.setrecursionlimit(1000)


def print_board(board):
        for i in board:
                o = 4 * i
                print("\n", end="")
                for u in o:
                        print("-", end="")
                print("\n", end="")
                for u in i:
                        if u != 0:
                                print(" " + str(u), end=" |")
                        else:
                                print("   ", end="|")

        print("\n")


def check_row(board, x, number):
        for i in board[x]:
                if i == number:
                        return False
        return True


def check_column(board, y, number):
        for i in board:
                if i[y] == number:
                        return False
        return True

def get_square_corner(x, y):

        if x > 5:
                if y > 5:
                        return [6, 6]
                elif y > 2:
                        return [6, 3]
                else:
                        return [6, 0]
        elif x > 2:
                if y > 5:
                        return [3, 6]
                elif y > 2:
                        return [3, 3]
                else:
                        return [3, 0]
        else:
                if y > 5:
                        return [0, 6]
                elif y > 2:
                        return [0, 3]
                else:
                        return [0, 0]


def check_square(board, x, y, number):
        square_corner = get_square_corner(x, y)

        # coordenada x do canto superior esquerdo desse quadrado
        m = square_corner[0]
        # coordenada y do canto superior esquerdo desse quadrado
        n = square_corner[1]

        g = m + 3
        h = n + 3
        for i in range(m, g):
                for j in range(n, h):
                        if board[i][j] == number:
                                return False
        return True


def is_pos_valid(board, x, y, number, invalid_positions):
        if [x, y] in invalid_positions:
                return False
        elif number < 1 or number > 9 or x < 0 or y < 0 or x > 8 or y > 8:
                return False
        elif check_row(board, x, number) and check_column(board, y, number):
                if check_square(board, x, y, number):
                        return True
        return False


def no_empty_spaces(board):
        for i in board:
                for j in i:
                        if j == 0:
                                return False
        return True


def backtracking_solver(x, y, board, invalid_positions):
        if no_empty_spaces(board):
                return 1
        solution = -1
        i = 0
        if [x, y] in invalid_positions:
                if y == 8:
                        return backtracking_solver(x + 1, 0, board, invalid_positions)
                else:
                        return backtracking_solver(x, y + 1, board, invalid_positions)
        else:
                while(solution == -1 and i < 10):
                        i += 1
                        if is_pos_valid(board, x, y, i, invalid_positions):

                                board[x][y] = i
                                if y == 8:
                                        solution = backtracking_solver(
                                            x + 1, 0, board, invalid_positions)
                                else:
                                        solution = backtracking_solver(
                                            x, y + 1, board, invalid_positions)
                        if solution == -1:
                                board[x][y] = 0

        return solution

def main():

        board = [[0, 0, 1, 2, 0, 7, 0, 0, 0], [0, 6, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 9, 4, 0], [0, 0, 0, 9, 8, 0, 0, 0, 3], [
            5, 0, 0, 0, 0, 0, 0, 0, 0], [7, 0, 0, 0, 3, 0, 0, 2, 1], [0, 0, 0, 1, 0, 2, 0, 0, 0], [0, 7, 0, 8, 0, 0, 4, 1, 0], [3, 0, 4, 0, 0, 0, 0, 8, 0]]

        easy_board = [[0, 0, 0, 1, 9, 0, 8, 7, 6], [0, 1, 8, 0, 0, 0, 0, 0, 0], [6, 0, 4, 3, 5, 0, 0, 0, 0], [0, 0, 0, 0, 3, 7, 9, 0, 0], [
            4, 8, 3, 0, 0, 0, 2, 0, 7], [0, 0, 0, 2, 0, 6, 3, 0, 5], [2, 3, 6, 7, 8, 0, 0, 9, 0], [0, 5, 0, 4, 0, 0, 0, 1, 0], [0, 0, 0, 5, 0, 0, 0, 3, 2]]

        invalid_positions = []
        for i in range(9):
                for j in range(9):
                        if board[i][j] != 0:
                                invalid_positions.append([i, j])

        print_board(board)

        backtracking_solver(0, 0, board, invalid_positions)
        print_board(board)


main()
