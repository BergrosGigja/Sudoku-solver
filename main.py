import pygame

def isValid(grid, i, j, check):
    for x in range(9):
        if str(check) == grid[i][x]:
            return False
    for x in range(9):
        if str(check) == grid[x][j]:
            return False
    boxX = 3 *(i//3)
    boxY = 3 *(j//3)
    for x in range(boxX, boxX+3):
        for y in range(boxY, boxY+3):
            if grid[x][y] == str(check):
                return False
    return True

def solveSudoku(grid, i=0, j=0):
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

    for check in range(1,10):
        if isValid(grid,i,j,check):
            grid[i][j] = str(check)
            if solveSudoku(grid):
                return True
            grid[i][j] = ""
    return False

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

def vertical(screen, color):
    pygame.draw.lines(screen, color, False, [(0,0), (400,0)], 4)
    pygame.draw.lines(screen, color, False, [(0,44), (400,44)], 1) #First small line
    pygame.draw.lines(screen, color, False, [(0,88), (400,88)], 1) #Second small line
    pygame.draw.lines(screen, color, False, [(0,132), (400,132)], 4) #First thick line
    pygame.draw.lines(screen, color, False, [(0,176), (400,176)], 1) #third small line
    pygame.draw.lines(screen, color, False, [(0,220), (400,220)], 1) #fourth small line
    pygame.draw.lines(screen, color, False, [(0,264), (400,264)], 4) #Second thick line
    pygame.draw.lines(screen, color, False, [(0,308), (400,308)], 1) #fifth small line
    pygame.draw.lines(screen, color, False, [(0,352), (400,352)], 1) #sixth small line
    pygame.draw.lines(screen, color, False, [(0,396), (400,396)], 4)

def horizontal(screen, color):
    pygame.draw.lines(screen, color, False, [(0,0), (0,400)], 4)
    pygame.draw.lines(screen, color, False, [(44,0), (44,400)], 1) #First small line
    pygame.draw.lines(screen, color, False, [(88,0), (88,400)], 1) #Second small line
    pygame.draw.lines(screen, color, False, [(132,0), (132,400)], 4) #First thick line
    pygame.draw.lines(screen, color, False, [(176,0), (176,400)], 1) #third small line
    pygame.draw.lines(screen, color, False, [(220,0), (220,400)], 1) #fourth small line
    pygame.draw.lines(screen, color, False, [(264,0), (264,400)], 4) #Second thick line
    pygame.draw.lines(screen, color, False, [(308,0), (308,400)], 1) #fifth small line
    pygame.draw.lines(screen, color, False, [(352,0), (352,400)], 1) #sixth small line
    pygame.draw.lines(screen, color, False, [(396,0), (396,400)], 4)
 
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

    button = pygame.Rect(0, 398, 398, 100)

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    solveSudoku(grid, 0, 0)
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

        pygame.draw.rect(screen, GREEN, button)
        solve = font.render("SOLVE", True, BLACK)
        solve_rect = solve.get_rect()
        text_x = 200 - solve_rect.width / 2
        text_y = 450 - solve_rect.height / 2
        screen.blit(solve, [text_x, text_y])
                                
        pygame.display.flip()

if __name__=="__main__":
    main()