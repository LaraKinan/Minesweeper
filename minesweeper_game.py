from minesweeper_class import minesweepers_board
from button_class import Button
from colors import *
import pygame
        
def new_game(board: minesweepers_board):
    # initialize board
    board.board = board.init_board()
    board.fill_board()

    board.dug = set()
    board.flagged = set()
    global safe, game_running
    safe = True
    game_running = True

def draw_board(board: minesweepers_board, revealed, new_game_button):
    for row in range(board.dim_size):
        for col in range(board.dim_size):
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if (row, col) in revealed:
                if board.board[row][col] == 0:
                    pygame.draw.rect(screen, DARK_GRAY, cell_rect)
                elif board.board[row][col] == '*':
                    # Resize the bomb image to fit the cell
                    pygame.draw.rect(screen, GRAY, cell_rect)
                    resized_bomb_image = pygame.transform.scale(bomb_image, (CELL_SIZE, CELL_SIZE))
                    screen.blit(resized_bomb_image, cell_rect)  # Draw the resized bomb image
                else:
                    pygame.draw.rect(screen, DARK_GRAY, cell_rect)
                    cell_value = str(board.board[row][col])
                    text_color = RED if cell_value == '*' else get_color(board.board[row][col])
                    text = font.render(cell_value, True, text_color)
                    text_rect = text.get_rect(center=cell_rect.center)
                    screen.blit(text, text_rect)
            elif (row, col) in board.flagged:
                # Draw flag image on flagged cells
                pygame.draw.rect(screen, GRAY, cell_rect)
                resized_flag_image = pygame.transform.scale(flag_image, (CELL_SIZE, CELL_SIZE))
                screen.blit(resized_flag_image, cell_rect)
            else:
                pygame.draw.rect(screen, GRAY, cell_rect)
            
            # Draw cell borders
            pygame.draw.rect(screen, (128, 128, 128), cell_rect, BORDER_SIZE)

            if not (row, col) in revealed: # This is to add a 3D element to the cells
                
                # Draw darker borders for right and bottom
                pygame.draw.line(screen, DARK_GRAY, (cell_rect.bottomleft[0] + 1, cell_rect.bottomleft[1] - 1), (cell_rect.bottomright[0], cell_rect.bottomright[1] - 1), BORDER_SIZE)
                pygame.draw.line(screen, DARK_GRAY, (cell_rect.bottomright[0] - 1, cell_rect.bottomright[1] - 1), (cell_rect.topright[0] - 1, cell_rect.topright[1] - 1), BORDER_SIZE)
                
                # Draw lighter borders for top and left
                pygame.draw.line(screen, WHITE, (cell_rect.topleft[0] + 1, cell_rect.topleft[1] + 1), (cell_rect.topright[0] + 1, cell_rect.topright[1] + 1), BORDER_SIZE)
                pygame.draw.line(screen, WHITE, (cell_rect.topleft[0] + 1, cell_rect.topleft[1]), (cell_rect.bottomleft[0] + 1, cell_rect.bottomleft[1] - 1), BORDER_SIZE)

    # Draw the remaining bombs display
    remaining_bombs = board.num_bombs - len(board.flagged)
    remaining_bombs_text = remaining_bombs_font.render(f"Flags Left: {remaining_bombs}", True, RED)
    remaining_bombs_rect = remaining_bombs_text.get_rect(bottomleft=(10, screen_height - 10))
    screen.blit(remaining_bombs_text, remaining_bombs_rect)
    new_game_button.draw(screen, font)

def play(dim_size=10, num_bombs=10):
    global screen_running, safe, game_running
    board = minesweepers_board(dim_size, num_bombs)
    new_game_button = Button(screen_width - 150, screen_height - 40, 140, 30, "New Game", lambda: new_game(board))
    while screen_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    new_game_button.handle_event(event)
                    if game_running:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        clicked_row = mouse_y // CELL_SIZE
                        clicked_col = mouse_x // CELL_SIZE
                        safe = board.dig(clicked_row, clicked_col)

                        if not safe:
                            break
                elif event.button == 3 and game_running:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    clicked_row = mouse_y // CELL_SIZE
                    clicked_col = mouse_x // CELL_SIZE
                    if (clicked_row, clicked_col) not in board.dug:
                        if (clicked_row, clicked_col) in board.flagged:
                            board.flagged.remove((clicked_row, clicked_col))
                        elif not board.num_bombs == len(board.flagged):
                            board.flagged.add((clicked_row, clicked_col))

        # Clear the screen
        screen.fill(WHITE)

        # Draw the board
        draw_board(board, board.dug, new_game_button)
        
        # Check game over conditions
        if len(board.dug) == board.dim_size ** 2 - board.num_bombs:
            text = font.render("CONGRATULATIONS! YOU WIN!", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)
            game_running = False
        elif not safe:
            text = font.render("GAME OVER! BETTER LUCK NEXT TIME :(", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)
            game_running = False
        
        pygame.display.flip()
    # Quit pygame
    pygame.quit()

# initializing pygame parameters
pygame.init()

# Set up the game window
DIM_SIZE = 20
NUM_BOMBS = DIM_SIZE * 3
WIDTH, HEIGHT = 600, 600
screen_width, screen_height = WIDTH, 650
CELL_SIZE = WIDTH // DIM_SIZE
BORDER_SIZE = 2  # Define the border size

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minesweeper")

font = pygame.font.Font(None, 36)

# Load the bomb and flag images
bomb_image = pygame.image.load('bomb_image.png')
flag_image = pygame.image.load('flag_image.png')

# Font for the remaining bombs display
remaining_bombs_font = pygame.font.Font(None, 24)

# Initialize global values
safe = True 
screen_running = True
game_running = True
play(DIM_SIZE, NUM_BOMBS)