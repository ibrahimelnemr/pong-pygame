from game import game

class draw:
    
    def draw_game_screen():
        player_score_text_surface = game.text_font.render(f"Player score: {game.scores[0]}", True, game.text_color)
        enemy_score_text_surface = game.text_font.render(f"Enemy score: {game.scores[1]}", True, game.text_color)

        player_score_text_surface_rect = player_score_text_surface.get_rect()
        enemy_score_text_surface_rect = enemy_score_text_surface.get_rect()


        player_score_text_surface_rect.center = game.player_score_pos
        enemy_score_text_surface_rect.center = game.enemy_score_pos

        game.screen.blit(player_score_text_surface, player_score_text_surface_rect)
        game.screen.blit(enemy_score_text_surface, enemy_score_text_surface_rect)

        game.player_object.draw(game.screen)
        game.enemy_object.draw(game.screen)
        game.ball_object.draw(game.screen)

    def draw_welcome_message():
        message = "Welcome to Pong! Press any key to begin or q to quit."
        message_text_surface = game.text_font.render(message,True, game.text_color)
        message_text_surface_rect = message_text_surface.get_rect()
        
        message_text_surface_rect.center = game.message_pos

        game.screen.blit(message_text_surface, message_text_surface_rect)

    def draw_end_screen():
        message = "Game over. "
        if game.scores[0] > game.scores [1]:
            message += "Player 1 wins. "
        else:
            message += "Player 2 wins. "
        
        message += "\nPress any key to play again."
        
        message_text_surface = game.text_font.render(message,True, game.text_color)
        message_text_surface_rect = message_text_surface.get_rect()
        
        message_text_surface_rect.center = game.message_pos

        game.screen.blit(message_text_surface, message_text_surface_rect)