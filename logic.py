import pygame
from game import game

class logic:

    def handle_movement():
        keys = pygame.key.get_pressed()

        # move player bat
        if keys[pygame.K_UP] and game.player_object.pos_y > 0:
            game.player_object.move("UP")
        if keys[pygame.K_DOWN] and game.player_object.pos_y < game.HEIGHT - game.player_object.height:
            game.player_object.move("DOWN")

        # move ball
        game.ball_object.move()        

        # move enemy bat automatically
        if game.enemy_object.pos_y > game.ball_object.pos_y:
            game.enemy_object.dir_y = -1
        elif game.enemy_object.pos_y < game.ball_object.pos_y:
            game.enemy_object.dir_y = 1

        # if enemy_object.pos_y > HEIGHT or enemy_object.pos_y < 0:
        #     enemy_object.dir_y *= -1

        game.enemy_object.move()

        # move enemy bat by input (optional)
        # if keys[pygame.K_w] and enemy_object.pos_y > 0:
        #     enemy_object.pos_y -= enemy_object.vel
        # if keys[pygame.K_s] and enemy_object.pos_y < HEIGHT - enemy_object.height:
        #     enemy_object.pos_y += enemy_object.vel

    def handle_collisions():

        if game.ball_object.pos_x > game.WIDTH:
            game.ball_object.pos_x = game.WIDTH // 2
            # ball_object.dir_x *= -1
            game.scores[0] += 1
        if game.ball_object.pos_x < 0:
            game.ball_object.pos_x = game.WIDTH // 2
            # ball_object.dir_x *= -1
            game.scores[1] += 1

        
        if game.ball_object.pos_y > game.HEIGHT or game.ball_object.pos_y < 0:
            game.ball_object.dir_y *= -1
        
        # handle collision with ball and player bat
        if game.ball_object.pos_x in range(game.player_object.pos_x, game.player_object.pos_x + game.player_object.width) and game.ball_object.pos_y in range(game.player_object.pos_y, game.player_object.pos_y + game.player_object.height): 
            game.ball_object.dir_x *= -1

        # handle collision with ball and enemy bat
        if game.ball_object.pos_x in range(game.enemy_object.pos_x - game.ball_object.width, game.enemy_object.pos_x - game.ball_object.width + game.enemy_object.width) and game.ball_object.pos_y in range(game.enemy_object.pos_y, game.enemy_object.pos_y + game.enemy_object.height): 
            game.ball_object.dir_x *= -1