import random


def print_board(board):
    for i in range(3):
        print(f" {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} ")
        if i < 2:
            print("-----------")


def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None


def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def find_best_move(board, difficulty):
    # Common checks for Medium and Hard levels
    if difficulty in ['medium', 'hard']:
        # Check for immediate win
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                if check_winner(board):
                    board[i] = ' '
                    return i
                board[i] = ' '

        # Check for block
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                if check_winner(board):
                    board[i] = ' '
                    return i
                board[i] = ' '

    # Difficulty-specific logic
    if difficulty == 'hard':
        best_score = -float('inf')
        best_move = -1
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    elif difficulty == 'medium':
        # Random choice after basic checks
        empty_spots = [i for i, spot in enumerate(board) if spot == ' ']
        return random.choice(empty_spots)

    elif difficulty == 'easy':
        # Purely random moves
        empty_spots = [i for i, spot in enumerate(board) if spot == ' ']
        return random.choice(empty_spots)


def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe with difficulty levels!")
    print("Choose computer difficulty:")
    print("1. Easy (Random moves)")
    print("2. Medium (Basic strategy)")
    print("3. Hard (Unbeatable)")

    while True:
        level = input("Enter difficulty level (1-3): ")
        if level in ['1', '2', '3']:
            difficulty = ['easy', 'medium', 'hard'][int(level) - 1]
            break
        print("Invalid input. Please enter 1, 2, or 3.")

    print("\nYou are X and the computer is O.")
    print("Enter positions (1-9) as shown below:")
    print_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    print("\nLet's start!\n")

    while True:
        if current_player == 'X':
            print_board(board)
            while True:
                position = input("Your turn (1-9): ")
                try:
                    position = int(position) - 1
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")
                    continue

                if position < 0 or position >= 9:
                    print("Position out of range. Please choose a number between 1 and 9.")
                    continue

                if board[position] != ' ':
                    print("That position is already taken. Choose another.")
                    continue

                break
        else:
            # Computer's turn
            position = find_best_move(board, difficulty)
            print(f"\nComputer chooses position {position + 1}")

        board[position] = current_player

        # Print the board after computer's move
        if current_player == 'O':
            print_board(board)

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'X':
                print("Congratulations! You win!")
            else:
                print("Computer wins!")
            break

        if ' ' not in board:
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()
