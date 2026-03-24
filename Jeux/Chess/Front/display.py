from assets import load_assets
import pygame
import copy
pygame.init()
screen = pygame.display.set_mode((700, 700))
chessboard, pieces = load_assets()
pygame.display.set_caption("Chess")
king_white = pieces[0]
king_black = pieces[1]
queen_white = pieces[2]
queen_black = pieces[3]
bishop_white = pieces[4]
bishop_black = pieces[5]
knight_white = pieces[6]
knight_black = pieces[7]
rook_white = pieces[8]
rook_black = pieces[9]
pawn_white = pieces[10]
pawn_black = pieces[11]

piece_dict = {
    'king_white': king_white,
    'king_black': king_black,
    'queen_white': queen_white,
    'queen_black': queen_black,
    'bishop_white': bishop_white,
    'bishop_black': bishop_black,
    'knight_white': knight_white,
    'knight_black': knight_black,
    'rook_white': rook_white,
    'rook_black': rook_black,
    'pawn_white': pawn_white,
    'pawn_black': pawn_black
}

grid = [[None for _ in range(8)] for _ in range(8)]

position_to_algebraic = {(column, row): chr(64 + column) + str(9 - row) 
                         for column in range(1, 9) for row in range(1, 9)}

def place_piece(piece, column, row):
    grid[row-1][column-1] = [piece, (55 + (column-1) * 80, 15 + (row-1) * 80), column, row]

def is_on_board(column, row):
    return 1 <= row <= 8 and 1 <= column <= 8

def initialize_board():
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            place_piece(None, cell + 1, row + 1)
            
    place_piece('rook_black', 1, 1)
    place_piece('knight_black', 2, 1)
    place_piece('bishop_black', 3, 1)
    place_piece('queen_black', 4, 1)
    place_piece('king_black', 5, 1)
    place_piece('bishop_black', 6, 1)
    place_piece('knight_black', 7, 1)
    place_piece('rook_black', 8, 1)
    for i in range(8):
        place_piece('pawn_black', i + 1, 2)

    place_piece('rook_white', 1, 8)
    place_piece('knight_white', 2, 8)
    place_piece('bishop_white', 3, 8)
    place_piece('queen_white', 4, 8)
    place_piece('king_white', 5, 8)
    place_piece('bishop_white', 6, 8)
    place_piece('knight_white', 7, 8)
    place_piece('rook_white', 8, 8)
    for i in range(8):
        place_piece('pawn_white', i + 1, 7)

def get_color(p):
    if p in ['king_white', 'queen_white', 'bishop_white', 'knight_white', 'rook_white', 'pawn_white']:
        return 'white'
    elif p in ['king_black', 'queen_black', 'bishop_black', 'knight_black', 'rook_black', 'pawn_black']:
        return 'black'
    return None

def get_moves(piece, column, row, grid):

    def is_empty(c, r):
        return grid[r-1][c-1][0] is None

    def is_enemy(c, r, my_color):
        p = grid[r-1][c-1][0]
        return p is not None and get_color(p) != my_color

    my_color = get_color(piece)

    def moves_king():
        candidates = [
            (column + 1, row), (column - 1, row), (column, row + 1), (column, row - 1),
            (column + 1, row + 1), (column + 1, row - 1), (column - 1, row + 1), (column - 1, row - 1)
        ]
        return [(c, r) for (c, r) in candidates if is_on_board(c, r) and (is_empty(c, r) or is_enemy(c, r, my_color))]

    def moves_knight():
        candidates = [
            (column + 2, row + 1), (column + 2, row - 1), (column - 2, row + 1), (column - 2, row - 1),
            (column + 1, row + 2), (column + 1, row - 2), (column - 1, row + 2), (column - 1, row - 2)
        ]
        return [(c, r) for (c, r) in candidates if is_on_board(c, r) and (is_empty(c, r) or is_enemy(c, r, my_color))]

    def moves_queen():
        result = []
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        for dc, dr in directions:
            for i in range(1, 8):
                c, r = column + i * dc, row + i * dr
                if not is_on_board(c, r): break
                if is_empty(c, r):
                    result.append((c, r))
                elif is_enemy(c, r, my_color):
                    result.append((c, r))
                    break
                else:  # own piece
                    break
        return result

    def moves_rook():
        result = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dc, dr in directions:
            for i in range(1, 8):
                c, r = column + i * dc, row + i * dr
                if not is_on_board(c, r): break
                if is_empty(c, r):
                    result.append((c, r))
                elif is_enemy(c, r, my_color):
                    result.append((c, r))
                    break
                else:  # own piece
                    break
        return result

    def moves_bishop():
        result = []
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for dc, dr in directions:
            for i in range(1, 8):
                c, r = column + i * dc, row + i * dr
                if not is_on_board(c, r): break
                if is_empty(c, r):
                    result.append((c, r))
                elif is_enemy(c, r, my_color):
                    result.append((c, r))
                    break
                else:  # own piece
                    break
        return result

    def moves_pawn_black():
        result = []
        # Single advance
        if row < 8 and is_empty(column, row + 1):
            result.append((column, row + 1))
            # Double advance from row 2
            if row == 2 and is_empty(column, row + 2):
                result.append((column, row + 2))
        # Diagonal captures
        if is_on_board(column + 1, row + 1) and is_enemy(column + 1, row + 1, my_color):
            result.append((column + 1, row + 1))
        if is_on_board(column - 1, row + 1) and is_enemy(column - 1, row + 1, my_color):
            result.append((column - 1, row + 1))
        # En passant
        if en_passant_target and row == 4 and en_passant_target[1] == 3 and (en_passant_target[0] == column + 1 or en_passant_target[0] == column - 1):
            result.append(en_passant_target)
        return result

    def moves_pawn_white():
        result = []
        # Single advance
        if row > 1 and is_empty(column, row - 1):
            result.append((column, row - 1))
            # Double advance from row 7
            if row == 7 and is_empty(column, row - 2):
                result.append((column, row - 2))
        # Diagonal captures
        if is_on_board(column + 1, row - 1) and is_enemy(column + 1, row - 1, my_color):
            result.append((column + 1, row - 1))
        if is_on_board(column - 1, row - 1) and is_enemy(column - 1, row - 1, my_color):
            result.append((column - 1, row - 1))
        # En passant
        if en_passant_target and row == 5 and en_passant_target[1] == 6 and (en_passant_target[0] == column + 1 or en_passant_target[0] == column - 1):
            result.append(en_passant_target)
        return result

    if piece == 'king_white' or piece == 'king_black':
        return moves_king()
    elif piece == 'knight_white' or piece == 'knight_black':
        return moves_knight()
    elif piece == 'queen_white' or piece == 'queen_black':
        return moves_queen()
    elif piece == 'rook_white' or piece == 'rook_black':
        return moves_rook()
    elif piece == 'bishop_white' or piece == 'bishop_black':
        return moves_bishop()
    elif piece == 'pawn_black':
        return moves_pawn_black()
    elif piece == 'pawn_white':
        return moves_pawn_white()

def is_in_check(color, grid):
    king = 'king_white' if color == 'white' else 'king_black'
    king_pos = None
    for r in range(8):
        for c in range(8):
            if grid[r][c][0] == king:
                king_pos = (c + 1, r + 1)
                break
    if not king_pos:
        return False
    opponent_color = 'black' if color == 'white' else 'white'
    for r in range(8):
        for c in range(8):
            piece = grid[r][c][0]
            if piece and get_color(piece) == opponent_color:
                moves = get_moves(piece, c + 1, r + 1, grid)
                if king_pos in moves:
                    return True
    return False

def get_legal_moves(piece, column, row, grid, color):
    possible_moves = get_moves(piece, column, row, grid)
    legal_moves = []
    for move in possible_moves:
        temp_grid = copy.deepcopy(grid)
        temp_grid[row-1][column-1] = [None, (55 + (column-1) * 80, 15 + (row-1) * 80), column, row]
        # Handle en passant in simulation
        if piece == 'pawn_white' and en_passant_target == move:
            temp_grid[move[1]-2][move[0]-1] = [None, (55 + (move[0]-1) * 80, 15 + (move[1]-2) * 80), move[0], move[1]-1]
        elif piece == 'pawn_black' and en_passant_target == move:
            temp_grid[move[1]][move[0]-1] = [None, (55 + (move[0]-1) * 80, 15 + move[1] * 80), move[0], move[1]+1]
        moved_piece = piece
        if piece == 'pawn_white' and move[1] == 1:
            moved_piece = 'queen_white'
        elif piece == 'pawn_black' and move[1] == 8:
            moved_piece = 'queen_black'
        temp_grid[move[1]-1][move[0]-1] = [moved_piece, (55 + (move[0]-1) * 80, 15 + (move[1]-1) * 80), move[0], move[1]]
        if not is_in_check(color, temp_grid):
            legal_moves.append(move)
    return legal_moves

selected_piece = None
possible_moves = []
current_turn = 'white'
game_over = False
promotion_pending = False
promotion_pos = None
promotion_color = None
en_passant_target = None

initialize_board()
while True:
    
    screen.fill((100, 100, 100))
    screen.blit(chessboard, (10, 10))
    for row in grid:
        for cell in row:
            if cell[0]:
                piece, pos, col, row = cell
                screen.blit(piece_dict[piece], pos)
    # Highlight possible moves
    if possible_moves:
        for c, r in possible_moves:
            center_x = 55 + (c-1) * 80 + 35
            center_y = 15 + (r-1) * 80 + 35
            pygame.draw.circle(screen, (100, 100, 100), (center_x, center_y), 10)
    # Draw promotion options
    if promotion_pending:
        # Draw semi-transparent background for selection
        promotion_bg = pygame.Surface((400, 80), pygame.SRCALPHA)
        promotion_bg.fill((200, 200, 200, 128))  # Semi-transparent light gray
        screen.blit(promotion_bg, (140, 295))
        options = [('queen', 150), ('rook', 250), ('bishop', 350), ('knight', 450)]
        for opt, x in options:
            piece_key = f'{opt}_{promotion_color}'
            screen.blit(piece_dict[piece_key], (x, 300))
    pygame.display.flip()

    
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    initialize_board()
                    selected_piece = None
                    possible_moves = []
                    current_turn = 'white'
                    game_over = False
                    promotion_pending = False
                    promotion_pos = None
                    promotion_color = None
                    en_passant_target = None
                    print("Game restarted!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if promotion_pending:
                if 300 <= pos[1] <= 370:  # Adjusted for new y position
                    options = [('queen', 150), ('rook', 250), ('bishop', 350), ('knight', 450)]
                    for opt, x in options:
                        if x <= pos[0] <= x + 70:
                            piece = f'{opt}_{promotion_color}'
                            place_piece(piece, promotion_pos[0], promotion_pos[1])
                            print(f"Promoted to {opt} at {position_to_algebraic[promotion_pos]}")
                            # Check for check
                            if is_in_check(current_turn, grid):
                                print(f"{current_turn.capitalize()} is in check!")
                            # Switch turn
                            current_turn = 'black' if current_turn == 'white' else 'white'
                            print(f"Turn: {current_turn}")
                            # Check for game end
                            all_moves = []
                            for r in range(8):
                                for c in range(8):
                                    p = grid[r][c][0]
                                    if p and get_color(p) == current_turn:
                                        all_moves.extend(get_legal_moves(p, c+1, r+1, grid, current_turn))
                            if not all_moves:
                                if is_in_check(current_turn, grid):
                                    print(f"Checkmate! {'White' if current_turn == 'white' else 'Black'} loses.")
                                else:
                                    print("Stalemate! Draw.")
                                game_over = True
                            promotion_pending = False
                            promotion_pos = None
                            promotion_color = None
                            break
            else:
                clicked_column = (pos[0] - 55) // 80 + 1
                clicked_row = (pos[1] - 15) // 80 + 1
                if not is_on_board(clicked_column, clicked_row):
                    continue
                if selected_piece:
                    piece, sel_column, sel_row = selected_piece
                    if (clicked_column, clicked_row) in possible_moves:
                        # Move the piece
                        grid[sel_row-1][sel_column-1] = [None, (55 + (sel_column-1) * 80, 15 + (sel_row-1) * 80), sel_column, sel_row]
                        # Handle en passant capture
                        if piece == 'pawn_white' and en_passant_target == (clicked_column, clicked_row):
                            grid[clicked_row-2][clicked_column-1] = [None, (55 + (clicked_column-1) * 80, 15 + (clicked_row-2) * 80), clicked_column, clicked_row-1]
                        elif piece == 'pawn_black' and en_passant_target == (clicked_column, clicked_row):
                            grid[clicked_row][clicked_column-1] = [None, (55 + (clicked_column-1) * 80, 15 + clicked_row * 80), clicked_column, clicked_row+1]
                        # Set en passant target
                        en_passant_target = None
                        if piece == 'pawn_white' and sel_row == 7 and clicked_row == 5:
                            en_passant_target = (clicked_column, 6)
                        elif piece == 'pawn_black' and sel_row == 2 and clicked_row == 4:
                            en_passant_target = (clicked_column, 3)
                        # Handle pawn promotion
                        if piece == 'pawn_white' and clicked_row == 1:
                            promotion_pending = True
                            promotion_pos = (clicked_column, clicked_row)
                            promotion_color = 'white'
                        elif piece == 'pawn_black' and clicked_row == 8:
                            promotion_pending = True
                            promotion_pos = (clicked_column, clicked_row)
                            promotion_color = 'black'
                        else:
                            place_piece(piece, clicked_column, clicked_row)
                            print(f"Moved to {position_to_algebraic[(clicked_column, clicked_row)]}")
                            # Check for check
                            if is_in_check(current_turn, grid):
                                print(f"{current_turn.capitalize()} is in check!")
                            # Switch turn
                            current_turn = 'black' if current_turn == 'white' else 'white'
                            print(f"Turn: {current_turn}")
                            # Check for game end
                            all_moves = []
                            for r in range(8):
                                for c in range(8):
                                    p = grid[r][c][0]
                                    if p and get_color(p) == current_turn:
                                        all_moves.extend(get_legal_moves(p, c+1, r+1, grid, current_turn))
                            if not all_moves:
                                if is_in_check(current_turn, grid):
                                    print(f"Checkmate! {'White' if current_turn == 'white' else 'Black'} loses.")
                                else:
                                    print("Stalemate! Draw.")
                                game_over = True
                    selected_piece = None
                    possible_moves = []
                else:
                    cell = grid[clicked_row-1][clicked_column-1]
                    if cell[0]:
                        piece = cell[0]
                        piece_color = get_color(piece)
                        if piece_color == current_turn:
                            selected_piece = (piece, clicked_column, clicked_row)
                            possible_moves = get_legal_moves(piece, clicked_column, clicked_row, grid, current_turn)
                            print(f"Selected {piece_color} piece at {position_to_algebraic[(clicked_column, clicked_row)]}")
                            print("Possible moves:", [position_to_algebraic[(c, r)] for (c, r) in possible_moves])
                        else:
                            print(f"It's {current_turn}'s turn. Cannot select {piece_color} piece.")