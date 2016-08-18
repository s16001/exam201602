from tkinter import *
import random
import time

def point_collision(a, b):
    cx = (b[2] - b[0]) / 2
    cy = (b[3] - b[1]) / 2
    r = cx
    #left-top
    dx = cx - a[0]
    dy = cy - a[1]
    p1 = dx**2 + dy**2 < r**2
    #right-top
    dx = cx - a[2]
    dy = cy - a[1]
    p2 = dx**2 + dy**2 < r**2
    #right_bottom
    dx = cx - a[2]
    dy = cy - a[3]
    p3 = dx**2 + dy**2 < r**2
    #left_bottom
    dx = cx - a[0]
    dy = cy - a[3]
    p4 = dx**2 + dy**2 < r**2

    return p1 or p2 or p3 or p4

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.blocks = blocks
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = random.choice((-3, -2, -1, 1, 2, 3))
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

        return False

    def hit_block(self, pos):
        collision_type = 0
        for block in self.blocks:
            block_pos = self.canvas.coords(block.id)
            if point_collision(block_pos, pos):
                collision_type |= 3
            if pos[2] >= block_pos[0] and pos[0] <= block_pos[2] \
                    and pos[3] >= block_pos[1] and pos[3] <= block_pos[3]:
                collision_type |= 1
            if pos[2] >= block_pos[0] and pos[0] <= block_pos[2] \
                    and pos[1] > block_pos[1] and pos[1] <= block_pos[3]:
                collision_type |= 1
            if pos[3] >= block_pos[1] and pos[1] < block_pos[3] \
                    and pos[2] >= block_pos[0] and pos[2] < block_pos[2]:
                collision_type |= 2
            if pos[3] >= block_pos[1] and pos[1] <= block_pos[3] \
                    and pos[0] > block_pos[0] and pos[0] <= block_pos[2]:
                collision_type |= 2

            if collision_type != 0:
                return (block, collision_type)
        return (None, None)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y *= -1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = self.y * -1
        if pos[0] <= 0:
            self.x *= -1
        if pos[2] >= self.canvas_width:
            self.x *= -1

        (target, collision_type) = self.hit_block(pos)
        if target != None:
            target.delete()
            del self.blocks[self.blocks.index(target)]
            if (collision_type & 1) != 0:
                self.y *= -1
            if (collision_type & 2) != 0:
                self.x *= 1

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.started = False
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2

    def start_game(self, event):
        self.started = True

class Block:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.pos_x = x
        self.pos_y = y
        self.id = canvas.create_rectangle(0, 0, 30, 10, fill=color)
        self.canvas.move(self.id, 25 + self.pos_x * 50,
                         25 + self.pos_y * 20)

    def delete(self):
        self.canvas.delete(self.id)
class Gameover:
    def __init__(self, canvas, x, y, text, fontsize, color):
        self.canvas = canvas
        self.id = canvas.create_text(x, y, text=text, font=('Times', fontsize),
                                     fill=color, state='hidden')

    def show(self):
        self.canvas.itemconfig(self.id, state='normal')

WIDTH = 700
HEIGHT = 700
FPS = 100
BALL_SPEED = 5
PADDLE_SPEED = 3
COLORS = ('peachpuff', 'turquoise', 'dark orange', 'royal blue', 'brown',)

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
c = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
c.pack()
tk.update()

blocks = []
for y in range(5):
    for x in range(20):
        blocks.append(Block(c, x, y, random.choice(COLORS)))

p = Paddle(c, 'blue')
ball = Ball(c, p, 'red')

gameover = Gameover(c, 275, 275, "G A M E O V E R", 50, 'cyan')

def update():
    if not ball.hit_bottom:
        ball.draw()
        p.draw()

    tk.update_idletasks()
    tk.update()
    tk.after(10, update)


tk.after(10, update)
tk.mainloop()
