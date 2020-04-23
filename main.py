import pygame

# Is it valid for the rows and box
def isValid(grid, i, j, check):
    # Check if the number is in any of the other cells, vertical row
    for x in range(9):
        if str(check) == grid[i][x]:
            return False
    # Check if the number is in any of the other cells, horizontal row
    for x in range(9):
        if str(check) == grid[x][j]:
            return False
    # Check if the number is in any of the other cells, box
    boxX = 3 *(i//3)
    boxY = 3 *(j//3)
    for x in range(boxX, boxX+3):
        for y in range(boxY, boxY+3):
            if grid[x][y] == str(check):
                return False
    return True

# Solve sudoku
def solveSudoku(grid, i=0, j=0):
    #Find next empty cell
    changes = True
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == "":
                i = x
                j = y
                changes = False
                break
    if changes:
        return True

    # check rest of the gird if number will fit
    for check in range(1,10):
        if isValid(grid,i,j,check):
            grid[i][j] = str(check)
            if solveSudoku(grid):
                return True
            grid[i][j] = ""
    return False

def clear(grid):
    for x in range(0,9):
        for y in range(0,9):
            grid[x][y] = ""
    return False;

# Fill grid with numbers
def draw(grid, color, font, screen, WIDTH, HEIGHT):
    h = 1
    for row in range(9):
        w = 1
        for column in range(9):
            text = font.render(grid[row][column], True, color)
            text_rect = text.get_rect()
            text_x = ((w * (WIDTH + 4)) - WIDTH/2 ) - text_rect.width / 2
            text_y = ((h * (HEIGHT + 4)) - HEIGHT/2 ) - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            w += 1
        h += 1

# Draw vertical lines in grid
def vertical(screen, color):
    thickLine = 2
    for x in range(10):
        if thickLine == 2:
            pygame.draw.lines(screen, color, False, [(0,x*44), (400,x*44)], 4)
            thickLine = 0
        else:
            pygame.draw.lines(screen, color, False, [(0,x*44), (400,x*44)], 1)
            thickLine += 1

# Draw horizontal lines in grid
def horizontal(screen, color):
    thickLine = 2
    for x in range(10):
        if thickLine == 2:
            pygame.draw.lines(screen, color, False, [(x*44,0), (x*44,400)], 4)
            thickLine = 0
        else:
            pygame.draw.lines(screen, color, False, [(x*44,0), (x*44,400)], 1)
            thickLine += 1

def main():

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
    # Set WIDTH, HEIGHT AND MARGIN of grid
    WIDTH = 40
    HEIGHT = 40
    MARGIN = 4

    # Create a 2 dimensional array
    grid = []
    for row in range(9):
        grid.append([])
        for column in range(9):
            grid[row].append("")
     
    # initialize screen with logo and caption
    pygame.init()
    screen = pygame.display.set_mode((398,498))
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sudoku solver")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Font
    font = pygame.font.Font(None, 36)

    # Solve button
    button = pygame.Rect(0, 398, 398, 100)

    solved = False

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    if solved:
                        solved = clear(grid)
                    else:
                        solved = solveSudoku(grid, 0, 0)
                else:
                    # Change number based on mouse click
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)

                    if grid[row][column] == "":
                        grid[row][column] = "1"
                    elif grid[row][column] == "9":
                        grid[row][column] = ""
                    else:
                        newNum = int(grid[row][column]) + 1
                        grid[row][column] = str(newNum)

        screen.fill(WHITE)

        # Draw the grid
        horizontal(screen, BLACK)
        vertical(screen, BLACK)

        # Draw numbers
        draw(grid, BLACK, font, screen, WIDTH, HEIGHT)

        # Solve button
        if solved:
            pygame.draw.rect(screen, RED, button)
            solve = font.render("PLAY AGAIN", True, BLACK)
        else:
            pygame.draw.rect(screen, GREEN, button)
            solve = font.render("SOLVE", True, BLACK)

        solve_rect = solve.get_rect()
        text_x = 200 - solve_rect.width / 2
        text_y = 450 - solve_rect.height / 2
        screen.blit(solve, [text_x, text_y])
                                
        pygame.display.flip()

if __name__=="__main__":
    main()