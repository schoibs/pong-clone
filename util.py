import random

def draw_ball(screen, ball_rect, ball_surface, ball_x, ball_y, ):
    ball_rect.center = (ball_x, ball_y)
    screen.blit(ball_surface, ball_rect)

def draw_paddle(screen, paddle_rect, paddle_surface, paddle_x, paddle_y, isLeftPaddle):
    if (isLeftPaddle):
        paddle_rect.midleft = (paddle_x, paddle_y)
    else:
        paddle_rect.midright = (paddle_x, paddle_y)
    
    screen.blit(paddle_surface, paddle_rect)

def generate_movement_speed():
    random_speed = [-7, -6.5, 6.5, 7]
    return random.choice(random_speed)

def check_collision(paddle_rect_1, paddle_rect_2, ball_rect):
    if paddle_rect_2.colliderect(ball_rect) or paddle_rect_1.colliderect(ball_rect):
        return True

def ball_hit_boundary(ball_rect):
    if ball_rect.midtop[1] <= 0 or ball_rect.midbottom[1] >= 650:
        return True

def check_out_of_bound(ball_rect):
    if ball_rect.midright[0] <= 0:
        return 2 # Player 2 wins
    elif ball_rect.midright[0] >= 900:
        return 1 # Player 1 wins
    else:
        return 0