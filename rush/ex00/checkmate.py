def find_king(board):
    """Find the position of the King (K) on the board."""
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == 'K':
                return r, c
    return None

def is_valid_board(board):
    """Check if the board contains only allowed characters."""
    valid_pieces = {'K', 'P', 'B', 'R', 'Q', '.','-', '|'}
    for row in board:
        for cell in row:
            if cell not in valid_pieces:
                return False, cell  # Return the invalid character
    return True, None

def is_in_check(board, king_row, king_col):
    """Check if the King is in check by any piece."""
    
    # Check for Pawn attacks (only one step downward diagonally)
    for dr, dc in [(-1, -1), (-1, 1),(1, -1), (1, 1)]:  #  downward forward diagonals
        r, c = king_row + dr, king_col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'P':
            return True  # King is in check by a Pawn
    
    # Define movement rules for other pieces
    directions = {
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # Bishop moves diagonally
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # Rook moves straight
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]  # Queen moves diagonally and straight
    }

    # Check for Bishop, Rook, and Queen
    for piece, moves in directions.items():
        for dr, dc in moves:
            r, c = king_row + dr, king_col + dc
            while 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] == piece:
                    return True  # King is in check
                if board[r][c] != '.':  # Stop if another piece is blocking
                    break
                r += dr
                c += dc

    return False

def checkmate(board):
    """Main function to check if the King is in check."""
    
    # Validate the board first
    is_valid, invalid_char = is_valid_board(board)
    if not is_valid:
        print(f"Error: Invalid character '{invalid_char}' found on board.")
        return

    playable_pieces = {'P', 'B', 'R', 'Q'}
    # Check if there any player piece (P B R Q) & separate the wall & floor
    player_visible = any(any(piece in row for piece in playable_pieces) for row in board)
    # Count the number of Kings on the board
    king_count = sum(row.count('K') for row in board)
    if king_count > 1:
        print("Error: There are more than 1 King on the board.")
        return
    elif king_count == 1 and not player_visible:
        print("Error There are no Player here.")
        return
    elif king_count == 0:
        print("Error: No King on the board.")
        return


    # Check if the King is in check
    king_row, king_col = find_king(board)

    if is_in_check(board, king_row, king_col):
        print("Success")
    else:
        print("Fail")