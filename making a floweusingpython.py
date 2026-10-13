import turtle
import math

# -------------------- 1. SET UP THE WINDOW --------------------

screen = turtle.Screen()
screen.setup(width=850, height=700)
screen.title("A Little Flower Garden")
screen.bgcolor("#DFF6FF")
screen.tracer(0)

pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.penup()


# -------------------- 2. HELPER FUNCTIONS --------------------

def draw_polygon(points, fill_color, outline_color=None,
                 outline_width=1):

    if not points:
        return

    if outline_color is None:
        outline_color = fill_color

    pen.penup()
    pen.goto(points[0])
    pen.pensize(outline_width)
    pen.color(outline_color, fill_color)
    pen.pendown()
    pen.begin_fill()

    for point in points[1:]:
        pen.goto(point)

    pen.goto(points[0])
    pen.end_fill()
    pen.penup()


def draw_line(start, end, color, width=3):

    pen.penup()
    pen.goto(start)
    pen.pencolor(color)
    pen.pensize(width)
    pen.pendown()
    pen.goto(end)
    pen.penup()


def draw_dot(x, y, size, color):

    pen.penup()
    pen.goto(x, y)
    pen.dot(size, color)


def draw_cloud(x, y):

    draw_dot(x - 22, y, 34, "white")
    draw_dot(x, y + 10, 43, "white")
    draw_dot(x + 23, y, 32, "white")
    draw_dot(x + 3, y - 5, 30, "white")


# -------------------- 3. ROTATE POINTS --------------------

def rotate_point(cx, cy, along, across, angle_degrees):

    angle = math.radians(angle_degrees)

    x = (
        cx
        + along * math.cos(angle)
        - across * math.sin(angle)
    )

    y = (
        cy
        + along * math.sin(angle)
        + across * math.cos(angle)
    )

    return (x, y)


# -------------------- 4. DRAW A LEAF --------------------

def draw_leaf(x, y, angle, length, width, color):

    points = []
    steps = 30

    # Upper edge of the leaf
    for i in range(steps + 1):

        t = i / steps

        along = length * t
        across = width * math.sin(math.pi * t)

        points.append(
            rotate_point(x, y, along, across, angle)
        )

    # Lower edge of the leaf
    for i in range(steps, -1, -1):

        t = i / steps

        along = length * t
        across = -width * math.sin(math.pi * t)

        points.append(
            rotate_point(x, y, along, across, angle)
        )

    draw_polygon(
        points,
        color,
        outline_color="#237443",
        outline_width=1
    )


# -------------------- 5. DRAW A FLOWER PETAL --------------------

def draw_petal(cx, cy, angle, length, width,
               color, start=14):

    points = []
    steps = 30

    # First side of the petal
    for i in range(steps + 1):

        t = i / steps

        along = start + length * t
        across = width * math.sin(math.pi * t)

        points.append(
            rotate_point(cx, cy, along, across, angle)
        )

    # Second side of the petal
    for i in range(steps, -1, -1):

        t = i / steps

        along = start + length * t
        across = -width * math.sin(math.pi * t)

        points.append(
            rotate_point(cx, cy, along, across, angle)
        )

    draw_polygon(
        points,
        color,
        outline_color="#D94D78",
        outline_width=1
    )


# -------------------- 6. DRAW THE SKY --------------------

draw_cloud(-275, 225)
draw_cloud(95, 265)


# Draw the sun
sun_x, sun_y = 305, 245

draw_dot(sun_x, sun_y, 58, "#FFD166")
draw_dot(sun_x, sun_y, 42, "#FFE89A")


# Draw the sun's rays
for angle in range(0, 360, 45):

    a = math.radians(angle)

    start = (
        sun_x + 36 * math.cos(a),
        sun_y + 36 * math.sin(a)
    )

    end = (
        sun_x + 47 * math.cos(a),
        sun_y + 47 * math.sin(a)
    )

    draw_line(start, end, "#F4B942", width=3)


# -------------------- 7. DRAW THE GROUND --------------------

ground_points = [(-430, -350)]

for i in range(61):

    x = -430 + (860 / 60) * i

    y = -230 + 8 * math.sin(
        i / 60 * 2 * math.pi
    )

    ground_points.append((x, y))

ground_points.append((430, -350))

draw_polygon(
    ground_points,
    "#9BE7A3",
    outline_color="#76C982",
    outline_width=2
)


# Draw little grass strokes
for x in [-380, -325, -245, -175, 170, 245, 325, 385]:

    ground_y = -230 + 8 * math.sin(
        (x + 430) / 860 * 2 * math.pi
    )

    draw_line(
        (x, ground_y + 2),
        (x - 5, ground_y + 13),
        "#4DAD66",
        width=2
    )

    draw_line(
        (x, ground_y + 2),
        (x + 5, ground_y + 14),
        "#4DAD66",
        width=2
    )


# -------------------- 8. DRAW THE STEM --------------------

draw_line(
    (0, 95),
    (0, -235),
    "#2F8F50",
    width=10
)


# -------------------- 9. DRAW THE LEAVES --------------------

draw_leaf(
    0, -35,
    150,
    95,
    25,
    "#55C878"
)

draw_leaf(
    0, -100,
    28,
    88,
    23,
    "#38B96B"
)


# -------------------- 10. DRAW THE FLOWER --------------------

flower_x, flower_y = 0, 105

outer_colors = [
    "#FF6F91",
    "#FF85A1",
    "#FF9EB5",
    "#FF7898"
]

inner_colors = [
    "#FFC2D1",
    "#FFADC2",
    "#FFD0DB",
    "#FFA6BE"
]


# Draw 12 large outer petals
for i in range(12):

    angle = i * 30

    color = outer_colors[i % len(outer_colors)]

    draw_petal(
        flower_x,
        flower_y,
        angle,
        length=105,
        width=29,
        color=color,
        start=13
    )


# Draw 12 smaller inner petals
for i in range(12):

    angle = i * 30 + 15

    color = inner_colors[i % len(inner_colors)]

    draw_petal(
        flower_x,
        flower_y,
        angle,
        length=78,
        width=22,
        color=color,
        start=10
    )


# -------------------- 11. DRAW THE YELLOW CENTER --------------------

draw_dot(flower_x, flower_y, 54, "#E69B22")
draw_dot(flower_x, flower_y, 43, "#FFD166")


# Add tiny seed dots
for angle in range(0, 360, 24):

    a = math.radians(angle)

    x = flower_x + 14 * math.cos(a)
    y = flower_y + 14 * math.sin(a)

    draw_dot(x, y, 4, "#9C5B18")


# Small central dot
draw_dot(flower_x, flower_y, 8, "#F4A62A")


# -------------------- 12. ADD DECORATIONS --------------------

decorations = [
    (-155, 170, "#FFFFFF"),
    (145, 190, "#FFFFFF"),
    (-170, 45, "#FFE08A"),
    (165, 70, "#FFFFFF"),
    (235, 145, "#FFB3C7")
]

for x, y, color in decorations:

    draw_dot(x, y, 9, color)


# -------------------- 13. ADD THE TITLE --------------------

pen.goto(0, 305)

pen.color("#34718A")

pen.write(
    "A Little Flower Garden",
    align="center",
    font=("Arial", 20, "bold")
)


# -------------------- 14. FINISH --------------------

screen.update()

turtle.done()
