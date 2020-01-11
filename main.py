import pygame
from time import sleep
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
him = pygame.image.load('C:\\Users\\derpi\\Documents\\GitHub\\minesweeper\\him.png')
icon = pygame.image.load('C:\\Users\\derpi\\Documents\\GitHub\\minesweeper\\ico.png')
hands = pygame.image.load('C:\\Users\\derpi\\Documents\\GitHub\\minesweeper\\lapki.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Vibesweeper")
clock = pygame.time.Clock()

# def text_objects(text, font):
#     text_surface = font.render(text, True, black)
#     return text_surface, text_surface.get_rect()

# def main_menu():
#     menu = True
#     while menu:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 menu = False
#                 pygame.quit()
#                 quit()
#         screen.fill((0, 0, 0))
#         menutext = pygame.font.Font('arial.ttf', 115)
#         TextSurf, TextRect = text_objects('Vibesweeper', menutext)
#         TextRect.center = ((250), (250))
#         screen.blit(TextSurf, TextRect)
#         pygame.display.update()
#         clock.tick(15)

# main_menu()
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    # screen.blit(him, (60, 60))
    # pygame.display.update()
    # sleep(3)
    # screen.blit(hands, (30, 300))
    # deathsound = pygame.mixer.Sound('C:\\Users\derpi\Documents\GitHub\minesweeper\dead.wav')
    # deathsound.play()
    # pygame.display.update()
    # sleep(1)
    # running = False