import pygame
 
def main():
     
    # initialize screen with logo and caption
    pygame.init()
    screen = pygame.display.set_mode((480,360))
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sudoku solver")

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
     
if __name__=="__main__":
    main()