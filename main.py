import pygame
from logic import logic
from draw import draw
from game import game

pygame.font.init()
pygame.display.set_caption("Pong")

def main():
    screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
    clock = pygame.time.Clock()
    run = True

    show_welcome_screen = True
    show_game_screen = False
    show_end_screen = False

    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            # print(event)

            if event.type == pygame.QUIT:
                run = False
                break

            if keys[pygame.K_q]:
                print("QUITTING")
                run = False
                break

            if keys[pygame.K_r]:
                print("Restarting game [r]")
                show_welcome_screen = True
                show_game_screen = False
                show_end_screen = False

            if keys[pygame.K_e]:
                print("Ending game [e]")
                show_end_screen = True
                show_welcome_screen = False
                show_game_screen = False

            if event.type == pygame.KEYDOWN and show_welcome_screen:
                game.restart_game()
                show_game_screen = True
                show_welcome_screen = False

            if event.type == pygame.KEYDOWN and show_end_screen:
                # restart the game
                game.restart_game()
                show_game_screen = True
                show_end_screen = False

        logic.handle_movement()

        logic.handle_collisions()

        screen.fill("black")

        if show_welcome_screen:
            draw.draw_welcome_message()

        if show_game_screen:
            draw.draw_game_screen()

        if show_end_screen:

            draw.draw_end_screen()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
