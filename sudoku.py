

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
                if board[y] == number:
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


def is_pos_valid(board, x, y, number):
        if number < 1 or number > 9 or x < 0 or y < 0 or x > 8 or y > 8:
                return False
        elif board[x][y] != 0:
                return False
        elif check_row(board, x, number) and check_column(board, y, number):
                if check_square(board, x, y, number):
                        return True
        return False

def main():

        board = [[0, 0, 1, 2, 0, 7, 0, 0, 0], [0, 6, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 9, 4, 0], [0, 0, 0, 9, 8, 0, 0, 0, 3], [
            5, 0, 0, 0, 0, 0, 0, 0, 0], [7, 0, 0, 0, 3, 0, 0, 2, 1], [0, 0, 0, 1, 0, 2, 0, 0, 0], [0, 7, 0, 8, 0, 0, 4, 1, 0], [3, 0, 4, 0, 0, 0, 0, 8, 0]]

        print_board(board)

        print(is_pos_valid(board, 0, 0, 1))


main()
