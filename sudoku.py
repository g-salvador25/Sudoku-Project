import pygame, sys
from sudoku_generator import SudokuGenerator, generate_sudoku
from main import Board, Cell



def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 540))
    board = generate_sudoku(9, 30)
    board_obj = Board(540, 540, screen, board)
    board_obj.draw()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                clicked_cell = board_obj.click(x,y)
                if clicked_cell:
                    board_obj.select(*clicked_cell)
            elif event.type == pygame.KEYDOWN:
                if board_obj.selected_cell:
                    if event.key == pygame.K_RETURN:
                        board_obj.selected_cell.set_cell_value(value)
                    elif event.key == pygame.K_BACKSPACE:
                        board_obj.selected_cell.set_cell_value(0)
                        board_obj.selected_cell.set_sketched_value(0)
                    elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                        value = int(pygame.key.name(event.key))
                        board_obj.selected_cell.set_sketched_value(value)
        #screen.fill((255,255,255))
        board_obj.update_board()
        board_obj.draw()
        pygame.display.flip()


        if board_obj.is_full() and board_obj.check_board:
            print("Congratulations! You win!")
            break


if __name__ == '__main__':
    main()