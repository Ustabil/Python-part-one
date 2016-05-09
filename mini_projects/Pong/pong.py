# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2 - BALL_RADIUS / 2, HEIGHT / 2 - BALL_RADIUS / 2]
    # ball_vel = [3, random.randrange(-5, 5)]
    if direction == 'LEFT':
        vertical_vel = random.randrange(3, 5) * -1
    elif direction == 'RIGHT':
        vertical_vel = random.randrange(3, 5)
    ball_vel = [vertical_vel, random.randrange(1, 3) * -1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    paddle1_pos = 0
    paddle2_pos = 0

    if random.randrange(0, 1001) >= 500:
        spawn_ball('LEFT')
    else:
        spawn_ball('RIGHT')


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    paddle1_pos += 1

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS) or ball_pos[1] <= (0 + BALL_RADIUS):
        ball_vel[1] *= -1
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS, 1, 'Grey', 'Grey')

    # update paddle's vertical position, keep paddle on the screen

    # draw paddles
    #left paddle:
    canvas.draw_polygon([(0, (HEIGHT / 2) - HALF_PAD_HEIGHT + paddle1_pos), (PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT + paddle1_pos), (PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT + paddle1_pos), (0, (HEIGHT / 2) + HALF_PAD_HEIGHT + paddle1_pos)], 1, 'White', 'White')

    #right paddle:
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT + paddle2_pos), (WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT + paddle2_pos), (WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT + paddle2_pos), (WIDTH - PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT + paddle2_pos)], 1, 'White', 'White')

    # determine whether paddle and ball collide
    if ball_pos[0] < (0 + BALL_RADIUS):
        #Give point to right player
        print 'Point right'
        spawn_ball('RIGHT')

    elif ball_pos[0] > (WIDTH - BALL_RADIUS):
        #Give point to left player
        print 'Point left'
        spawn_ball('LEFT')


    # draw scores

def keydown(key):
    global paddle1_vel, paddle2_vel

def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
