import pygame

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))

def hub(): #ONLY USE THIS

        #Load Image
        menu_og = pygame.image.load('hub2.png').convert()
        move_og = pygame.image.load('move2.png').convert()

        scale = 0.5

        m_w = int(menu_og.get_width() * scale)
        m_h = int(menu_og.get_height() * scale)

        v_w = int(move_og.get_width() * scale)
        v_h = int(move_og.get_height() * scale)

        menu_og.set_colorkey((255, 255, 255))
        move_og.set_colorkey((255, 255, 255))

        menu = pygame.transform.smoothscale(menu_og, (m_w, m_h))
        move = pygame.transform.smoothscale(move_og, (v_w, v_h))

        menu_rect = menu.get_rect()
        move_rect = move.get_rect()

        #Position
        menu_rect.bottomleft = (0, screen_height)
        move_rect.bottomright = (screen_width, screen_height)

        playing = True

        while playing:

                screen.fill((0, 0, 0))


                screen.blit(menu, menu_rect)
                screen.blit(move, move_rect)

                pygame.display.flip()


                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                playing = False
        pygame.quit()

hub()