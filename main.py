import classes


game = classes.Game()
snake = classes.Snake(game.GREEN)
food = classes.Food(game.RED, game.WIDTH, game.HEIGHT)

classes.Game.init_and_check_for_errors()

while True:
    # Get direction
    snake.change_to = game.event_loop(snake.change_to)

    # Movement
    snake.validate_direction_and_change()
    snake.change_head_position()
    # Update (if it's need) score and food
    game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos,
                                                           game.WIDTH, game.HEIGHT)

    # Drawing
    snake.draw_snake(game.display_surface, game.BLACK)
    food.draw_food(game.display_surface)

    # Check for collisions
    snake.check_for_boundaries(game.game_over, game.WIDTH, game.HEIGHT)

    # Show and update screen
    game.show_score()
    game.update_screen()
