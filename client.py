import pygame
from network import Network
import pickle
from settings import RED, WIDTH, HEIGHT
from rendering import redrawWindow
from button import BTNS

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")
pygame.font.init()

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player:", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, RED)
            elif game.winner == -1:
                text = font.render("Tie Game!", 1, RED)
            else:
                text = font.render("You Lost!", 1, RED)

            win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in BTNS:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redrawWindow(win, game, player)


main()