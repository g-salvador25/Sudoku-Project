import pygame, sys
from sudoku_generator import SudokuGenerator, generate_sudoku


def draw_grid():
    for i in range(0, 10): #draws horizontal lines
        if i % 3 == 0:
            width = 7
        else:
            width = 3
        pygame.draw.line(screen,
                         (0,0,0),
                         (0, i * 60),
                         (540, i * 60),
                         width)

    for i in range(0, 10): #draws vertical lines
        if i % 3 == 0:
            width = 7
        else:
            width = 3
        pygame.draw.line(screen,
                         (0,0,0),
                         (i * 60, 0),
                         (i * 60, 540),
                         width)


def draw_num(obj, screen_obj):
    font = pygame.font.SysFont(None, 60)
    for row in range(9):
        for column in range(9):
            if obj[row][column] != 0:
                cell_num = obj[row][column]
                cell_text = font.render(str(cell_num), True, pygame.Color('black'))
                screen.blit(cell_text, pygame.Vector2((column*60)+20, (row*60)+15))

#def sketch_num(obj, screen_obj, num):



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((540,540)) #creates a screen of 540x540 pixels
    screen.fill((255, 255, 245)) #sets color of screen
    draw_grid()
    board = generate_sudoku(9,30) #creates board object from SudokuGenerator class
    draw_num(board, screen)



while True:
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == pygame.QUIT: sys.exit()


