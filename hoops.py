import arcade
import math
import random

WIDTH = 640
HEIGHT = 480

show_images = True
write_msg = False

msg_part1 = "!!!YOU ARE CURRENTLY IN UGLY MODE!!!"
msg_part2 = "!!!PLEASE MAKE SURE THAT YOU HAVE LOADED ALL THE IMAGES FROM MY GITHUB TO GO TO NORMAL MODE!!!"

# Buttons
#        x ,  y ,  w , h
play = [175, 210, 125, 50]

highscores = [325, 210, 125, 50]

instructions = [237.5, 140, 150, 50]

# net
#        x    ,  y , r
net = [WIDTH/2, 410, 40]
net_speed = 0

net_reset = False

net_right = True
net_left = False
net_up = False
net_down = False

try:
    net_img = arcade.load_texture("images/net.jpg")
except FileNotFoundError:
    show_images = False
    write_msg = True

# Ball
#        x    y   r
ball = [320, 115, 25]
ball_speed = 15
ball_reset = False

try:
    ball_img = arcade.load_texture("images/basketball.png")
except FileNotFoundError:
    show_images = False
    write_msg = True

# Aim
aim_x = 320
aim_y = 115
aim_right = False
aim_left = False
show_aim = True

# Shoot
shoot_ball = False

# Power up
#             x    ,  y , r
power_up = [WIDTH/2, 330, 15]
power_name = "none"
power_speed = 5

power_right = True
power_left = False
give_power = False

try:
    power_img = arcade.load_texture("images/power_up.png")
except FileNotFoundError:
    show_images = False
    write_msg = True

# Score
score = 0
final_score = 0
score_list = [0, 0, 0, 0, 0]

collision = False

# Health
health = 5

# Screens
current_screen = "Menu"

# Menu Screen Background
try:
    menu_background = arcade.load_texture("images/background.jpg")
except FileNotFoundError:
    show_images = False
    write_msg = True

# Instructions and Highscores Scree Background
try:
    other_background = arcade.load_texture("images/background2.jpg")
except FileNotFoundError:
    show_images = False
    write_msg = True


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Hoops")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global WIDTH, HEIGHT
    global net, net_right, net_left, net_up, net_down, net_speed, net_reset
    global ball, shoot_ball, ball_speed, ball_reset
    global aim_x, aim_y, aim_right, aim_left, show_aim
    global health, score, final_score
    global current_screen
    global give_power, power_up, power_left, power_right, power_speed, power_name
    global collision

    # Gameplay
    if current_screen == "Play":
        # net movement
        net_movement(75, WIDTH - 75, 410, 250)

        # Ball Shoot
        if shoot_ball is True:
            shoot()

        # Aim
        aim_movement(100, WIDTH-100)

        # Boundaries and Health
        if ball[1] >= HEIGHT or ball[0] <= 0 or ball[0] >= WIDTH:
            health -= 1
            ball_reset = True

        if health == 0:
            death()

        # Score Keeping
        check_collision(ball, net)

        if collision is True:
            ball_reset = True
            score += 1
            net_speed += 0.5

        # Power Ups
        if score % 10 == 0 and score != 0:
            give_power = True
        else:
            give_power = False

        if give_power is True:
            power_movement(WIDTH-150, 150)
            random_power()
            check_collision(ball, power_up)

            if collision is True:
                if power_name == "health":
                    score += 1
                    health += 1
                elif power_name == "slownet":
                    net_speed = 0.5
                    score += 1
                elif power_name == "scorebonus":
                    score += 5

                ball_reset = True
                give_power = False

    # Resetting Stuff
    if ball_reset is True:
        reset('ball')

    if net_reset is True:
        reset('net')

    if current_screen != "Play":
        reset('game')


def on_draw():
    global net, net_img
    global ball
    global aim_x, aim_y, show_aim
    global current_screen, menu_background
    global play, instructions, highscores
    global final_score
    global power_up, give_power
    global show_images

    arcade.start_render()
    # Draw in here...

    if current_screen == "Death":
        if write_msg is True:
            arcade.draw_text(msg_part1, 180, 450, arcade.color.RADICAL_RED, 10)
            arcade.draw_text(msg_part2, 10, 430, arcade.color.RADICAL_RED, 8)

        arcade.draw_text("You Died!!! (Press M to go to menu)", 85, HEIGHT/2, arcade.color.BLACK, 20)
        arcade.set_background_color(arcade.color.RED_DEVIL)

        arcade.draw_text(f"Final Score: {final_score}", WIDTH/2 - 80, HEIGHT/2 - 50, arcade.color.BLACK)

    if current_screen == "Menu":
        if write_msg is True:
            arcade.draw_text(msg_part1, 180, 450, arcade.color.RADICAL_RED, 10)
            arcade.draw_text(msg_part2, 10, 430, arcade.color.RADICAL_RED, 8)

        if show_images is True:
            arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, menu_background)

        arcade.set_background_color(arcade.color.WHITE)

        arcade.draw_text("Hoops", 256, HEIGHT * 2/3, arcade.color.BLACK, 30, italic=True)

        # Play Button
        arcade.draw_xywh_rectangle_filled(play[0], play[1], play[2], play[3], arcade.color.ORANGE)
        arcade.draw_text("Play", 215, 228, arcade.color.BLACK, 15)

        # Highscore Button
        arcade.draw_xywh_rectangle_filled(instructions[0], instructions[1], instructions[2], instructions[3], arcade.color.ORANGE)
        arcade.draw_text("Instructions", 254, 157, arcade.color.BLACK, 15)

        # Instructions Button
        arcade.draw_xywh_rectangle_filled(highscores[0], highscores[1], highscores[2], highscores[3], arcade.color.ORANGE)
        arcade.draw_text("Highscores", 332, 228, arcade.color.BLACK, 15)

    if current_screen == "Play":
        if write_msg is True:
            arcade.draw_text(msg_part1, 180, 450, arcade.color.RADICAL_RED, 10)
            arcade.draw_text(msg_part2, 10, 430, arcade.color.RADICAL_RED, 8)

        # background
        arcade.set_background_color(arcade.color.WHITE)

        # Bottom bar
        arcade.draw_rectangle_filled(WIDTH / 2, 30, WIDTH, 95, arcade.color.SOAP)

        arcade.draw_text("Press 'm' for menu", 260, 15, arcade.color.BLACK)

        # net
        arcade.draw_circle_filled(net[0], net[1], net[2], arcade.color.BLUE)

        if show_images is True:
            arcade.draw_texture_rectangle(net[0], net[1], net[2]*3, net[2]*2.5, net_img)

        # aim
        if show_aim is True:
            arcade.draw_line(320, 115, aim_x, aim_y, arcade.color.BLACK)

        # ball
        arcade.draw_circle_filled(ball[0], ball[1], ball[2], arcade.color.ORANGE)

        if show_images is True:
            arcade.draw_texture_rectangle(ball[0], ball[1], ball[2]*2, ball[2]*2, ball_img)

        # Health
        for x in range(health * 25, 24, -25):
            arcade.draw_xywh_rectangle_filled(x, 25, 20, 20, arcade.color.RADICAL_RED)

        arcade.draw_text("Health:", 25, 50, arcade.color.BLACK)

        # Score
        arcade.draw_text(f"Score: {score}", WIDTH-100, 40, arcade.color.BLACK, 13)

        # Power Up
        if give_power is True:
            arcade.draw_circle_filled(power_up[0], power_up[1], power_up[2], arcade.color.GREEN)

            if show_images is True:
                arcade.draw_texture_rectangle(power_up[0], power_up[1], power_up[2]*3, power_up[2]*3, power_img)

        arcade.draw_text(f" Last Power Up: {power_name}", 225, 40, arcade.color.CHARLESTON_GREEN, 15)

    if current_screen == "Highscores":
        if write_msg is True:
            arcade.draw_text(msg_part1, 180, 450, arcade.color.RADICAL_RED, 10)
            arcade.draw_text(msg_part2, 10, 430, arcade.color.RADICAL_RED, 8)

        if show_images is True:
            arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, other_background)

        arcade.set_background_color(arcade.color.WHITE)

        arcade.draw_text("Highscores", 200, HEIGHT * 4/5, arcade.color.BLACK, 30, italic=True)

        # Top 5 Highscores
        for num, value in enumerate(score_list):
            arcade.draw_text(f"{num+1}. {value}", 270, HEIGHT * 2/3 - num*50, arcade.color.BLACK, 15, italic=True)

        arcade.draw_text("Press 'm' for menu", 260, 15, arcade.color.BLACK)

    if current_screen == "Instructions":
        arcade.set_background_color(arcade.color.WHITE)

        arcade.draw_text("Instructions", 208, 425, arcade.color.BLACK, 30, italic=True)

        # Instructions
        # Shortcut keys
        arcade.draw_text("Shortcut Keys:", 45, 380, arcade.color.BLACK, 14)

        arcade.draw_text("-'m' takes you to the main menu", 80, 360, arcade.color.BLACK)
        arcade.draw_text("- 'i' takes you to the instructions screen", 80, 340, arcade.color.BLACK)
        arcade.draw_text("-'h' takes you to the top  5 highscores during your current session", 80, 320, arcade.color.BLACK)
        arcade.draw_text("-'p' start playing the game (only works from menu)", 80, 300, arcade.color.BLACK)

        # In-game controls
        arcade.draw_text("In-Game Controls:", 45, 270, arcade.color.BLACK, 14)

        arcade.draw_text("-Arrow keys to aim", 80, 250, arcade.color.BLACK)
        arcade.draw_text("-Space to shoot", 80, 230, arcade.color.BLACK)

        # Goal
        arcade.draw_text("Goal:", 45, 200, arcade.color.BLACK, 14)

        arcade.draw_text("-Get the ball in the net to earn points", 80, 180, arcade.color.BLACK)
        arcade.draw_text("-A power up will appear every 10 points you get", 80, 160, arcade.color.BLACK)
        arcade.draw_text("-The power up can be: Health, Slownet, or a Score bonus", 80, 140, arcade.color.BLACK)
        arcade.draw_text("-The aim of the game is to get a highscore before your lives run out ", 80, 120, arcade.color.BLACK)
        arcade.draw_text("-You can see you rtop 5 score on the highscores screen", 80, 100, arcade.color.BLACK)

        arcade.draw_text("Press 'm' for menu", 250, 15, arcade.color.BLACK)


def on_key_press(key, modifiers):
    global aim_left, aim_right
    global shoot_ball
    global current_screen
    global final_score, score

    # In-game Controls
    if key == arcade.key.LEFT and current_screen == "Play":
        aim_left = True
    elif key == arcade.key.RIGHT and current_screen == "Play":
        aim_right = True

    if key == arcade.key.SPACE and current_screen == "Play":
        shoot_ball = True

    # Shortcuts
    if key == arcade.key.M:
        current_screen = "Menu"

    if key == arcade.key.P and current_screen == "Menu":
        current_screen = "Play"

    if key == arcade.key.H:
        current_screen = "Highscores"

    if key == arcade.key.I:
        current_screen = "Instructions"


def on_key_release(key, modifiers):
    global aim_left, aim_right

    if key == arcade.key.LEFT:
        aim_left = False

    if key == arcade.key.RIGHT:
        aim_right = False


def on_mouse_press(x, y, button, modifiers):
    global play, instructions, highscores
    global current_screen

    if x > play[0] and x < play[0]+play[2] and y > play[1] and y < play[1]+play[3] and current_screen == "Menu":
        current_screen = "Play"

    if x > highscores[0] and x < highscores[0]+highscores[2] and y > highscores[1] and y < highscores[1]+highscores[3] and current_screen == "Menu":
        current_screen = "Highscores"

    if x > instructions[0] and x < instructions[0]+instructions[2] and y > instructions[1] and y < instructions[1]+instructions[3] and current_screen == "Menu":
        current_screen = "Instructions"


def net_movement(left_x, right_x, top_y, bottom_y):
    global net, net_speed, net_right, net_left, net_up, net_down

    if net[0] <= left_x and net[1] >= top_y:
        net_right = True
        net_left = False
        net_down = False
        net_up = False
    elif net[0] >= right_x and net[1] >= top_y:
        net_right = False
        net_left = False
        net_down = True
        net_up = False
    elif net[0] >= right_x and net[1] <= bottom_y:
        net_right = False
        net_left = True
        net_down = False
        net_up = False
    elif net[0] <= left_x and net[1] <= bottom_y:
        net_right = False
        net_left = False
        net_down = False
        net_up = True

    if net_right is True:
        net[0] += net_speed
    elif net_left is True:
        net[0] -= net_speed

    if net_down is True:
        net[1] -= net_speed
    elif net_up is True:
        net[1] += net_speed


def aim_movement(left_border, right_border):
    global aim_x, aim_right, aim_left
    global WIDTH

    if aim_left is True:
        aim_x -= 5
    elif aim_right is True:
        aim_x += 5

    if aim_x in range(right_border, WIDTH):
        aim_x = right_border
    elif aim_x in range(0, left_border):
        aim_x = left_border


def shoot():
    global aim_x, aim_y, show_aim
    global ball

    x_diff = aim_x - ball[0]
    y_diff = aim_y - ball[1]
    angle = math.atan2(y_diff, x_diff)

    ball_change_x = math.cos(angle) * ball_speed
    ball_change_y = math.sin(angle) * ball_speed

    ball[1] += ball_change_y
    ball[0] += ball_change_x

    aim_y += ball_change_y
    aim_x += ball_change_x

    show_aim = False


def check_collision(a, b):
    global collision

    dist_x = a[0] - b[0]
    dist_y = a[1] - b[1]

    dist = math.sqrt(dist_x ** 2 + dist_y ** 2)

    if dist < (a[2] + b[2] - 10):
        collision = True
    else:
        collision = False


def get_highscore(num):
    global score_list

    if num > score_list[4]:
        score_list.append(num)
        score_list.remove(min(score_list))
        score_list.sort(reverse=True)


def random_power():
    global give_power, power_name

    num = random.randrange(3)

    while power_name != "health" or power_name != "slownet" or power_name != "scorebonus":
        if give_power is True:
            if num == 0:
                power_name = "health"
                break
            elif num == 1:
                power_name = "slownet"
                break
            elif num == 2:
                power_name = "scorebonus"
                break


def power_movement(left_x, right_x):
    global WIDTH
    global power_up, power_left, power_right

    if power_up[0] >= left_x:
        power_left = True
        power_right = False
    elif power_up[0] <= right_x:
        power_left = False
        power_right = True

    if power_right is True:
        power_up[0] += power_speed
    elif power_left is True:
        power_up[0] -= power_speed


def reset(object):
    global net, net_speed, net_left, net_right, net_down, net_up, net_reset
    global ball, shoot_ball, ball_reset
    global aim_x, aim_y, show_aim
    global health, score

    # net reset
    if object == "net":
        net = [WIDTH / 2, 410, 40]
        net_speed = 0
        net_left = True
        net_right = False
        net_down = False
        net_up = False
        net_reset = False

    # ball reset
    if object == "ball":
        ball[0] = 320
        ball[1] = 115
        aim_x = 320
        aim_y = 215
        shoot_ball = False
        show_aim = True
        ball_reset = False

    # game reset
    if object == "game":
        ball_reset = True
        net_reset = True
        health = 5
        score = 0


def death():
    global current_screen
    global final_score, score
    global ball_reset
    global health
    global net_reset
    global power_name

    current_screen = "Death"
    final_score = score
    get_highscore(final_score)
    net_reset = True
    ball_reset = True
    power_name = "none"
    score = 0
    health = 5


if __name__ == '__main__':
    setup()
