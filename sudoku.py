

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

def get_square_center(x, y):

        if x > 5:
                if y > 5:
                        return [7, 7]
                elif y > 2:
                        return [7, 4]
                else:
                        return [7, 1]
        elif x > 2:
                if y > 5:
                        return [4, 7]
                elif y > 2:
                        return [4, 4]
                else:
                        return [4, 1]
        else:
                if y > 5:
                        return [1, 7]
                elif y > 2:
                        return [1, 4]
                else:
                        return [1, 1]


def check_square(board, x, y, number):
        square_center = get_square_center(x, y)

        # coordenada x do canto superior esquerdo desse quadrado
        m = square_center[0] - 1
        # coordenada y do canto superior esquerdo desse quadrado
        n = square_center[1] - 1

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
        elif board[x][y] != 0:
                return False
        elif check_row(board, x, number) and check_column(board, y, number):
                if check_square(board, x, y, number):
                        return True
        return False


def backtracking_solver(x, y, board, invalid_positions):
        found_solution = False
        if x < 0 or x > 8 or y < 0 or y > 8:
                return 1

        while([x, y] in invalid_positions):
                if y == 8:
                        y = 0
                        x += 1
                else:
                        y += 1

        if board[x][y] == 0:
                for u in range(1, 10):
                        if is_pos_valid(board, x, y, u, invalid_positions):
                                board[x][y] = u
                                found_solution = True
                                break
        else:
                for u in range(board[x][y], 10):
                        if is_pos_valid(board, x, y, u, invalid_positions):
                                board[x][y] = u
                                found_solution = True
                                break

        if found_solution == True:
                if y == 8:
                        backtracking_solver(x + 1, 0, board, invalid_positions)
                else:
                        backtracking_solver(x, y + 1, board, invalid_positions)
        else:
                if y == 0:
                        backtracking_solver(x - 1, 8, board, invalid_positions)
                else:
                        backtracking_solver(x, y - 1, board, invalid_positions)
        return 1

def main():

        board = [[0, 0, 1, 2, 0, 7, 0, 0, 0], [0, 6, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 9, 4, 0], [0, 0, 0, 9, 8, 0, 0, 0, 3], [
            5, 0, 0, 0, 0, 0, 0, 0, 0], [7, 0, 0, 0, 3, 0, 0, 2, 1], [0, 0, 0, 1, 0, 2, 0, 0, 0], [0, 7, 0, 8, 0, 0, 4, 1, 0], [3, 0, 4, 0, 0, 0, 0, 8, 0]]

        invalid_positions = []
        for i in range(9):
                for j in range(9):
                        if board[i][j] != 0:
                                invalid_positions.append([i, j])

        print_board(board)

        backtracking_solver(0, 0, board, invalid_positions)
        print_board(board)


main()
