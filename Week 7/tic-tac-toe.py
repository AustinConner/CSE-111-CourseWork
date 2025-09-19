X = ["X"]
O = ["O"]
B = [""]

board = [
    [B, B, B],
    [B, B, B],
    [B, B, B]
]

def display(board):
    for row in range(3):
        for col in range(3):
            print(board[row][col], end="")
        print()



display(board)