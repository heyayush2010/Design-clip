import tkinter as tk
import random
import math

# Colors of the fireworks 
firework_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black"]

timers = []  # Global timer list for scheduled tasks

def create_desert_scene(canvas):
    canvas.delete("all")
    for i in range(600):
        color = f'#{int(0x1E1E6F + (0x1F * i)):x}'
        canvas.create_line(0, i, 1200, i, fill=color)

    canvas.create_oval(950, 100, 1150, 300, fill='light gray', outline='light gray')
    canvas.create_oval(975, 125, 1125, 275, fill='white', outline='white')

    canvas.create_polygon(0, 650, 400, 600, 800, 650, 1200, 600, 1200, 650,
                          fill='sandy brown', outline='sandy brown')

    canvas.create_polygon(100, 500, 400, 250, 700, 500, fill='dim gray', outline='dim gray')
    canvas.create_polygon(300, 500, 600, 200, 900, 500, fill='gray', outline='gray')
    canvas.create_polygon(500, 500, 800, 250, 1200, 500, fill='dark gray', outline='dark gray')

    canvas.create_polygon(250, 220, 300, 180, 350, 220, fill='light gray', outline='light gray')
    canvas.create_polygon(450, 120, 500, 80, 550, 120, fill='light gray', outline='light gray')

    canvas.create_polygon(400, 600, 450, 530, 550, 550, 650, 540, 750, 560, 850, 550, 1100, 600,
                          fill='deepskyblue', outline='deepskyblue')
    canvas.create_polygon(400, 610, 450, 540, 550, 560, 650, 550, 750, 570, 850, 560, 1100, 610,
                          fill='blue', outline='blue')

    for i in range(300):
        x = random.randint(0, 1200)
        y = random.randint(0, 400)
        size = random.randint(1, 3)
        canvas.create_oval(x, y, x+size, y+size, fill='white', outline='white')

    add_cactus(canvas, 150, 550)
    add_cactus(canvas, 350, 570)
    add_cactus(canvas, 800, 530)
    add_cactus(canvas, 1000, 550)

    add_bush(canvas, 200, 560)
    add_bush(canvas, 700, 560)

def add_cactus(canvas, x, y):
    canvas.create_rectangle(x-10, y-60, x+10, y, fill='green', outline='green')
    canvas.create_rectangle(x-30, y-40, x-10, y-20, fill='green', outline='green')
    canvas.create_rectangle(x+10, y-40, x+30, y-20, fill='green', outline='green')

def add_bush(canvas, x, y):
    for i in range(5):
        canvas.create_oval(x-10+i*5, y-10, x+10+i*5, y+10, fill='forest green', outline='forest green')

def create_sunset_scene(canvas):
    canvas.delete("all")
    for i in range(600):
        if i < 300:
            color = f'#{int(0x6B1A28 + (0x1F * i)):x}'
        else:
            color = f'#{int(0xFF8C00 + (0x1F * (i-300))):x}'
        canvas.create_line(0, i, 1200, i, fill=color)

    canvas.create_oval(950, 350, 1150, 550, fill='yellow', outline='yellow')

    canvas.create_polygon(0, 650, 400, 600, 800, 650, 1200, 600, 1200, 650,
                          fill='sandy brown', outline='sandy brown')

    for i in range(10):
        x1 = random.randint(50, 1150)
        x2 = x1 + random.randint(100, 300)
        height = random.randint(100, 350)
        canvas.create_rectangle(x1, 650-height, x2, 650, fill='gray', outline='gray')

    for i in range(15):
        x1 = random.randint(50, 1150)
        x2 = x1 + random.randint(50, 100)
        height = random.randint(50, 200)
        canvas.create_rectangle(x1, 650-height, x2, 650, fill='dim gray', outline='dim gray')
def create_shipwreck_scene(canvas):
    canvas.delete("all")
    for i in range(600):
        color_value = int(0x003366 + (0x1F * i))
        color = f'#{color_value:06x}'
        canvas.create_line(0, i, 1200, i, fill=color)

    canvas.create_polygon(400, 500, 600, 400, 800, 500, 1200, 400, 1200, 500,
                          fill='gray', outline='gray')

    canvas.create_line(500, 400, 500, 300, fill='saddlebrown', width=6)
    canvas.create_line(700, 400, 700, 300, fill='saddlebrown', width=6)

    canvas.create_rectangle(550, 480, 650, 500, fill='dim gray', outline='dim gray')
    canvas.create_line(600, 470, 650, 490, fill='black', width=2)

    for i in range(10):
        x = random.randint(100, 1100)
        y = random.randint(300, 600)
        canvas.create_oval(x, y, x+20, y+10, fill='yellow', outline='yellow')

    for i in range(5):
        x = random.randint(50, 1150)
        canvas.create_line(x, 500, x, 550, fill='green', width=4)

def create_cave_scene(canvas):
    canvas.delete("all")
    for i in range(600):
        color_value = int(0x3E1F0A + (0x1F * i))
        color = f'#{color_value:06x}'
        canvas.create_line(0, i, 1200, i, fill=color)

    for i in range(10):
        x1 = random.randint(100, 1100)
        x2 = x1 + random.randint(10, 40)
        canvas.create_line(x1, 50, x2, 100, fill='saddlebrown', width=random.randint(2, 5))

    for i in range(8):
        x1 = random.randint(100, 1100)
        x2 = x1 + random.randint(10, 40)
        height = random.randint(60, 120)
        canvas.create_polygon(x1, 650, x2, 650, x2, 650-height, x1, 650-height,
                              fill='saddlebrown', outline='saddlebrown')

    for i in range(5):
        x = random.randint(100, 1100)
        canvas.create_line(x, 600, x, 550, fill='green', width=3)

def create_forest_scene(canvas):
    canvas.delete("all")
    for i in range(600):
        color_value = int(0x4E8B3F + (0x1F * i))
        color = f'#{color_value:06x}'
        canvas.create_line(0, i, 1200, i, fill=color)

    for i in range(20):
        x = random.randint(50, 1150)
        y = random.randint(400, 600)
        tree_type = random.choice(['pine', 'oak', 'palm'])
        if tree_type == 'pine':
            add_pine_tree(canvas, x, y)
        elif tree_type == 'oak':
            add_oak_tree(canvas, x, y)
        elif tree_type == 'palm':
            add_palm_tree(canvas, x, y)

def add_pine_tree(canvas, x, y):
    canvas.create_polygon(x-20, y-50, x+20, y-50, x, y-150,
                          fill='forest green', outline='forest green')
    canvas.create_rectangle(x-5, y-50, x+5, y, fill='saddlebrown', outline='saddlebrown')

def add_oak_tree(canvas, x, y):
    canvas.create_oval(x-30, y-70, x+30, y-30, fill='dark green', outline='dark green')
    canvas.create_rectangle(x-10, y-30, x+10, y, fill='saddlebrown', outline='saddlebrown')

def add_palm_tree(canvas, x, y):
    canvas.create_rectangle(x-5, y-80, x+5, y, fill='saddlebrown', outline='saddlebrown')
    for i in range(5):
        canvas.create_line(x, y-80, x + random.randint(-30, 30), y-150,
                           fill='green', width=3)

def create_hills_valleys_scene(canvas):
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 1200, 700, fill='skyblue', outline='skyblue')

    for i in range(5):
        points = []
        for x in range(-100, 1300, 100):
            y = 500 - (i * 40) + random.randint(-20, 20)
            points.append((x, y))
        points.append((1200, 700))
        points.append((0, 700))
        flat_points = [coord for point in points for coord in point]
        canvas.create_polygon(flat_points, fill='green', outline='darkgreen')

    canvas.create_polygon(300, 600, 400, 550, 600, 560, 800, 580, 1000, 600,
                          900, 650, 300, 650, fill='deepskyblue', outline='blue')

def create_island_scene(canvas):
    canvas.delete("all")
    for i in range(600):
        color = f'#{int(0x0000CD + (i * 0x15)):06x}'
        canvas.create_line(0, i, 1200, i, fill=color)

    canvas.create_oval(450, 400, 750, 600, fill='sandybrown', outline='peru')
    canvas.create_oval(475, 425, 725, 575, fill='forestgreen', outline='darkgreen')

    for x in [525, 600, 675]:
        add_palm_tree(canvas, x, 470)

    canvas.create_polygon(100, 620, 150, 610, 180, 620, 140, 630,
                          fill='brown', outline='black')
def draw_sunset(canvas):
    for i in range(0, 300):
        red = int(255 - (i * 0.5))
        green = int(100 + (i * 0.5))
        blue = int(i * 0.8)
        color = f'#{red:02x}{green:02x}{blue:02x}'
        canvas.create_line(0, i, 1200, i, fill=color)

def draw_mountains(canvas):
    canvas.create_polygon(0, 250, 200, 150, 400, 250, 800, 150, 1200, 250, 1200, 300, 0, 300,
                          fill="gray", outline="black")
    canvas.create_polygon(0, 275, 200, 200, 400, 275, 800, 200, 1200, 275, 1200, 300, 0, 300,
                          fill="dimgray", outline="black")

def draw_river(canvas):
    canvas.create_polygon(0, 350, 1200, 350, 1200, 400, 0, 400, fill="blue", outline="blue")
    canvas.create_polygon(0, 375, 1200, 375, 1200, 425, 0, 425, fill="skyblue", outline="skyblue")

def draw_trees(canvas):
    tree_positions = [100, 300, 500, 700, 900, 1100]
    for x in tree_positions:
        trunk_height = random.randint(40, 60)
        foliage_size = random.randint(50, 80)
        canvas.create_rectangle(x - 10, 400 - trunk_height, x + 10, 400, fill="saddlebrown", outline="saddlebrown")
        canvas.create_oval(x - foliage_size // 2, 400 - trunk_height - foliage_size,
                           x + foliage_size // 2, 400 - trunk_height, fill="forestgreen", outline="forestgreen")

def draw_houses(canvas):
    house_positions = [50, 170, 290, 410, 530, 650, 770, 890, 1010]
    for x in house_positions:
        house_width = 80
        house_height = 100
        roof_height = 40
        canvas.create_rectangle(x, 500, x + house_width, 500 - house_height, fill="burlywood", outline="black")
        canvas.create_polygon(x, 500 - house_height, x + house_width // 2, 500 - house_height - roof_height,
                              x + house_width, 500 - house_height, fill="firebrick", outline="black")
        canvas.create_rectangle(x + 15, 500 - house_height + 20, x + 30, 500 - house_height + 35,
                                fill="lightblue", outline="black")
        canvas.create_rectangle(x + 50, 500 - house_height + 20, x + 65, 500 - house_height + 35,
                                fill="lightblue", outline="black")
        canvas.create_rectangle(x + 30, 500 - house_height + 50, x + 50, 500 - house_height + 85,
                                fill="peru", outline="black")

def draw_clouds(canvas):
    for _ in range(5):
        cloud_x = random.randint(50, 1150)
        cloud_y = random.randint(50, 150)
        cloud_size = random.randint(60, 100)
        canvas.create_oval(cloud_x, cloud_y, cloud_x + cloud_size, cloud_y + 30, fill="white", outline="white")
        canvas.create_oval(cloud_x + 20, cloud_y - 20, cloud_x + cloud_size - 20, cloud_y + 10,
                           fill="white", outline="white")

def draw_motorway_scene(canvas):
    canvas.delete("all")
    canvas.create_rectangle(0, 100, 1200, 400, fill="forestgreen", outline="forestgreen")
    canvas.create_rectangle(0, 150, 1200, 250, fill="gray", outline="gray")

    for i in range(0, 1200, 40):
        canvas.create_line(i, 200, i+20, 200, fill="white", width=2)

    canvas.create_rectangle(550, 175, 650, 200, fill="red", outline="red")
    canvas.create_oval(560, 190, 580, 210, fill="black")
    canvas.create_oval(620, 190, 640, 210, fill="black")

def draw_moon(canvas):
    canvas.create_oval(650, 50, 750, 150, fill="lightyellow", outline="lightyellow")

# --- Fireworks ---
firework_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white", "black"]

class FireworkSpark:
    def __init__(self, x, y, angle, speed, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.color = color
        self.distance_travelled = 0
        self.max_distance = random.uniform(100, 200)

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.distance_travelled += self.speed

    def is_done(self):
        return self.distance_travelled >= self.max_distance

def animate_firework(x, y, root):
    num_sparks = random.randint(100, 200)
    sparks = []
    for _ in range(num_sparks):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(4, 8)
        color = random.choice(firework_colors)
        sparks.append(FireworkSpark(x, y, angle, speed, color))

    def update_fireworks():
        canvas.delete("firework")
        sparks_to_remove = []
        for spark in sparks:
            spark.move()
            if not spark.is_done():
                canvas.create_oval(spark.x, spark.y, spark.x + 2, spark.y + 2,
                                   fill=spark.color, outline=spark.color, tags="firework")
            else:
                sparks_to_remove.append(spark)
        for spark in sparks_to_remove:
            sparks.remove(spark)
        if sparks:
            root.after(30, update_fireworks)

    update_fireworks()

def draw_scene(root, canvas):
    canvas.delete("all")
    draw_moon(canvas)
    draw_river(canvas)

    def animate_multiple_fireworks():
        for _ in range(5):
            x = random.randint(100, 1100)
            y = random.randint(100, 300)
            animate_firework(x, y, root)

    animate_multiple_fireworks()

def create_beach_scene(canvas):
    canvas.delete("all")

    # Sunset gradient
    for i in range(300):
        red = 255
        green = max(100 - i // 3, 0)
        blue = max(100 - i // 2, 0)
        color = f'#{red:02x}{green:02x}{blue:02x}'
        canvas.create_line(0, i, 1200, i, fill=color)

    # Sun
    canvas.create_oval(950, 100, 1050, 200, fill="yellow", outline="yellow")

    # Ocean
    canvas.create_rectangle(0, 300, 1200, 500, fill="deepskyblue", outline="deepskyblue")

    # Sun reflection on water
    for i in range(10):
        canvas.create_line(980 - i * 5, 300 + i * 5, 1020 + i * 5, 300 + i * 5,
                           fill="#ffd700", width=2)

    # Sand
    canvas.create_rectangle(0, 500, 1200, 700, fill="orange", outline="orange")

    # Coconut Tree
    x = 200
    y = 500
    for i in range(10):
        canvas.create_rectangle(x - 5 + i//2, y - i * 10 - 10, x + 5 + i//2, y - i * 10,
                                fill="saddlebrown", outline="saddlebrown")
    frond_length = 70
    angles = [-60, -30, 0, 30, 60]
    for angle in angles:
        for j in range(3):
            dx = frond_length * math.cos(math.radians(angle + j*4))
            dy = frond_length * math.sin(math.radians(angle + j*4))
            canvas.create_line(x + 10, y - 100, x + 10 + dx, y - 100 + dy,
                               fill="darkgreen", width=3)
    for i in range(3):
        canvas.create_oval(x + 3 + i*4, y - 92, x + 10 + i*4, y - 85,
                           fill="sienna", outline="sienna", tags="coconut")

    # Campfire
    cx, cy = 1000, 600
    for _ in range(6):
        angle = random.uniform(0, 2 * math.pi)
        dx = 15 * math.cos(angle)
        dy = 15 * math.sin(angle)
        canvas.create_line(cx, cy, cx + dx, cy + dy, fill="sienna", width=3)
    canvas.create_oval(cx - 10, cy - 20, cx + 10, cy, fill="orange red", outline="red")

    # Umbrella
    ux, uy = 800, 520
    canvas.create_line(ux, uy, ux, uy + 80, fill="tan", width=5)
    canvas.create_polygon(ux - 40, uy, ux, uy - 40, ux + 40, uy,
                          fill="crimson", outline="darkred")

    # --- Animated Waves ---
    def draw_wave(offset=0):
        for i in range(0, 1200, 80):
            canvas.create_arc(i + offset, 470, i + 80 + offset, 490,
                              start=0, extent=180, style=tk.ARC,
                              outline="white", width=2, tags="wave")

    def animate_waves():
        canvas.delete("wave")
        offset = random.randint(0, 40)
        draw_wave(offset)
        root.after(500, animate_waves)
    animate_waves()

    # --- Bobbing Boat ---
    boat = {"x": 600, "y": 420, "direction": 1}
    def draw_boat():
        bx, by = boat["x"], boat["y"]
        canvas.delete("boat")
        canvas.create_polygon(bx - 30, by, bx + 30, by,
                              bx + 20, by + 20, bx - 20, by + 20,
                              fill="saddlebrown", outline="black", tags="boat")
        canvas.create_line(bx, by, bx, by - 40, fill="black", width=2, tags="boat")
        canvas.create_polygon(bx, by - 40, bx + 20, by - 20, bx, by - 20,
                              fill="white", outline="black", tags="boat")

    def animate_boat():
        boat["y"] += boat["direction"]
        if boat["y"] > 425 or boat["y"] < 415:
            boat["direction"] *= -1
        draw_boat()
        root.after(100, animate_boat)
    draw_boat()
    animate_boat()

    # --- Flying Birds ---
    bird_positions = [(100, 100), (150, 130), (200, 90)]
    for bx, by in bird_positions:
        canvas.create_line(bx, by, bx + 10, by - 5, fill="black", width=2)
        canvas.create_line(bx + 10, by - 5, bx + 20, by, fill="black", width=2)

# --- Main App ---
def main():
    global root, canvas
    root = tk.Tk()
    root.title("Design Clip")
    canvas = tk.Canvas(root, width=1200, height=700, bg="black")
    canvas.pack()

    create_desert_scene(canvas)

    global timers
    timers = []
    timers.append(root.after(10000, lambda: create_sunset_scene(canvas)))
    timers.append(root.after(20000, lambda: create_shipwreck_scene(canvas)))
    timers.append(root.after(30000, lambda: create_cave_scene(canvas)))
    timers.append(root.after(40000, lambda: create_forest_scene(canvas)))
    timers.append(root.after(50000, lambda: create_hills_valleys_scene(canvas)))
    timers.append(root.after(60000, lambda: create_island_scene(canvas)))
    timers.append(root.after(70000, lambda: (canvas.delete("all"), draw_sunset(canvas),
                                             draw_mountains(canvas), draw_river(canvas),
                                             draw_trees(canvas), draw_houses(canvas),
                                             draw_clouds(canvas))))
    timers.append(root.after(80000, lambda: (canvas.delete("all"), draw_sunset(canvas),
                                             draw_mountains(canvas), draw_river(canvas),
                                             draw_trees(canvas), draw_houses(canvas),
                                             draw_clouds(canvas))))
    timers.append(root.after(90000, lambda: draw_motorway_scene(canvas)))
    timers.append(root.after(100000, lambda: draw_scene(root, canvas)))
    timers.append(root.after(110000, lambda: create_beach_scene(canvas)))

    def on_close():
        while timers:
            timer = timers.pop()
            try:
                root.after_cancel(timer)
            except Exception as e:
                print(f"Error canceling timer: {e}")
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
    main()
