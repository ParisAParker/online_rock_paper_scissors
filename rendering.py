import pygame
from settings import RED, GREEN, BLUE, BLACK
from button import BTNS

def redrawWindow(win, game, p):
    win.fill((128,128,128))

    if not (game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, RED, True)
        
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", 1, GREEN)
        win.blit(text, 80,200)

        text = font.render("Opponents", 1, (GREEN))
        win.blit(text, (380,200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        if game.bothWent():
            text1 = font.render(move1, 1, BLACK)
            text2 = font.render(move2, 1, BLACK)
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, BLACK)
            elif game.p1Went:
                text1 = font.render("Locked In", 1, BLACK)
            else:
                text1 = font.render("Waiting...", 1, BLACK)

            if game.p2Went and p == 0:
                text2 = font.render(move2, 1, BLACK)
            elif game.p1Went:
                text2 = font.render("Locked In", 1, BLACK)
            else:
                text2 = font.render("Waiting...", 1, BLACK)

        if p == 0:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))
        else:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))

        for btn in BTNS:
            btn.draw(win)
    
    pygame.display.update()