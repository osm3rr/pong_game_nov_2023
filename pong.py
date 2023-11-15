# setup
import pygame, sys

# funtions
def ball_animation():
	global ball_speed_x, ball_speed_y

	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if (ball.top <= 0) or (ball.bottom >= screen_height):
		ball_speed_y *= -1

	if (ball.left <= 0) or (ball.right >= screen_width):
		ball_speed_x *= -1

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

def player_animation():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opponent_animation():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height 

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')

# game rectangles
# ball
left_ball = (screen_width / 2) - 15
top_ball = (screen_height / 2) - 15
width_ball = 30
height_ball = 30

# player
player_left = screen_width - 20
player_top = (screen_height / 2) - 70
width_player = 10
height_player = 140

# opponent
opponent_left = 10
opponent_top = (screen_height / 2) - 70
width_opponent = width_player
height_opponent = height_player



ball = pygame.Rect(left_ball, top_ball, width_ball, height_ball)
player = pygame.Rect(player_left, player_top, width_player, height_player)
opponent = pygame.Rect(opponent_left, opponent_top, width_opponent, height_opponent)

# Game varibles
speed = 10
ball_speed_x = speed
ball_speed_y = speed
player_speed = 0
opponent_speed = speed

control = True
while control:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -= speed
			if event.key == pygame.K_DOWN:
				player_speed += speed

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed += speed
			if event.key == pygame.K_DOWN:
				player_speed -= speed

	# game logic
	ball_animation()
	player_animation()
	opponent_animation()

	# elements
	screen.fill(bg_color)
	pygame.draw.ellipse(screen, light_grey, ball)
	pygame.draw.rect(screen, light_grey, player)
	pygame.draw.rect(screen, light_grey, opponent)
	# Central line
	pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

	pygame.display.flip()
	clock.tick(60)