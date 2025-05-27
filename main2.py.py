from board import GameBoard
from ai import ai_pick

def main():
    board = GameBoard()
    print("Welcome to Tic-Tac-Toe!")
    print("You're X, and the AI is O. Let's begin!")
    board.show()

    while not board.finished():
        if board.turn == 'X':
            try:
                move = int(input("Your turn! Pick a spot (0-8): "))
            except ValueError:
                print("Oops! Please enter a number between 0 and 8.")
                continue

            if not board.place(move):
                print("That spot is already taken or invalid.")
                continue
        else:
            print("AI is thinking...")
            move = ai_pick(board)
            board.place(move)
            print(f"AI picked spot {move}.")

        board.show()

    # Final result
    winner = board.check_winner()
    if winner == 'O':
        print("The AI wins. Better luck next time!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
