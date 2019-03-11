import pygame

def draw(grid, color, font, screen, WIDTH, HEIGHT):
    h = 1
    for row in range(9):
        w = 1
        for column in range(9):

            text = font.render(grid[row][column], True, color)
            text_rect = text.get_rect()
            text_x = (w * WIDTH) - text_rect.width / 2
            text_y = (h * HEIGHT) - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            w += 1
        h += 1

def vertical(screen, color):
    pygame.draw.lines(screen, color, False, [(0,0), (400,0)], 4)
    pygame.draw.lines(screen, color, False, [(0,44), (400,44)], 1) #First small line
    pygame.draw.lines(screen, color, False, [(0,90), (400,90)], 1) #Second small line
    pygame.draw.lines(screen, color, False, [(0,133), (400,133)], 4) #First thick line
    pygame.draw.lines(screen, color, False, [(0,177), (400,177)], 1) #third small line
    pygame.draw.lines(screen, color, False, [(0,221), (400,221)], 1) #fourth small line
    pygame.draw.lines(screen, color, False, [(0,265), (400,265)], 4) #Second thick line
    pygame.draw.lines(screen, color, False, [(0,309), (400,309)], 1) #fifth small line
    pygame.draw.lines(screen, color, False, [(0,353), (400,353)], 1) #sixth small line
    pygame.draw.lines(screen, color, False, [(0, 398), (400, 398)], 4)

def horizontal(screen, color):
    pygame.draw.lines(screen, color, False, [(0,0), (0,400)], 4)
    pygame.draw.lines(screen, color, False, [(44,0), (44,400)], 1) #First small line
    pygame.draw.lines(screen, color, False, [(90,0), (90,400)], 1) #Second small line
    pygame.draw.lines(screen, color, False, [(133,0), (133,400)], 4) #First thick line
    pygame.draw.lines(screen, color, False, [(177,0), (177,400)], 1) #third small line
    pygame.draw.lines(screen, color, False, [(221,0), (221,400)], 1) #fourth small line
    pygame.draw.lines(screen, color, False, [(265,0), (265,400)], 4) #Second thick line
    pygame.draw.lines(screen, color, False, [(309,0), (309,400)], 1) #fifth small line
    pygame.draw.lines(screen, color, False, [(353,0), (353,400)], 1) #sixth small line
    pygame.draw.lines(screen, color, False, [(398,0), (398,400)], 4)
 
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
    screen = pygame.display.set_mode((400,500))
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sudoku solver")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Font
    font = pygame.font.Font(None, 36)

    button = pygame.Rect(0, 400, 400, 100)

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    print("solve")
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
        draw(grid, RED, font, screen, WIDTH, HEIGHT)

        pygame.draw.rect(screen, GREEN, button)
        solve = font.render("SOLVE", True, BLACK)
        solve_rect = solve.get_rect()
        text_x = 200 - solve_rect.width / 2
        text_y = 450 - solve_rect.height / 2
        screen.blit(solve, [text_x, text_y])
                                
        pygame.display.flip()

if __name__=="__main__":
    main()