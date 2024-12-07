import turtle


def orientation(p, q, r):
    """Return the orientation of the triplet (p, q, r).
       >0 : p->q->r is a left turn
       <0 : p->q->r is a right turn
       =0 : p, q, r are collinear
    """
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def convex_hull(points):
    """Compute the convex hull of a set of 2D points using Andrew's monotone chain algorithm."""
    points = sorted(points)  # Sort by x, then by y

    # Build the lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull
    return lower[:-1] + upper[:-1]


def draw_points_and_hull(all_points, hull_points, count_on_hull, title="Convex Hull with M"):
    screen = turtle.Screen()
    screen.title(title)
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Determine suitable scaling
    xs = [p[0] for p in all_points]
    ys = [p[1] for p in all_points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    offset = 1
    screen.setworldcoordinates(min_x - offset, min_y - offset, max_x + offset, max_y + offset)

    hull_set = set(hull_points)

    # Draw all points
    for p in all_points:
        t.penup()
        t.goto(p[0], p[1])
        if p in hull_set:
            t.dot(10, "red")  # Points on the hull larger and in red
        else:
            t.dot(5, "black")

    # Draw hull polygon
    if hull_points:
        t.color("red")
        t.penup()
        t.goto(hull_points[0][0], hull_points[0][1])
        t.pendown()
        for h in hull_points[1:]:
            t.goto(h[0], h[1])
        t.goto(hull_points[0][0], hull_points[0][1])

    # After drawing, write a message depending on the number of hull vertices
    t.penup()
    # Move turtle to a suitable place to write the message
    t.goto((min_x + max_x) / 2, max_y + 0.5)
    message = f"The hull has {len(hull_points)} vertices.\n"
    if len(hull_points) == 4:
        message += "This is a case with 4 vertices."
    elif len(hull_points) == 5:
        message += "This is a case with 5 vertices."
    else:
        message += "Different number of vertices."

    t.write(message, align="center", font=("Arial", 16, "normal"))

    t.hideturtle()
    screen.mainloop()


# Points for Part 2
A = (3, -3)
B = (3, 3)
C = (-3, -3)
D = (-3, 3)

# Choose a lambda value
# Try lambda_value = 0 for one configuration, or experiment with others like lambda_value = 1 or lambda_value = 2
lambda_value = 0
M = (-2 + lambda_value, 3 - lambda_value)

my_points = [A, B, C, D, M]
hull_part2 = convex_hull(my_points)

# Count how many of A,B,C,D,M are on the hull
hull_set = set(hull_part2)
count_on_hull = sum(1 for p in my_points if p in hull_set)

print(f"For λ={lambda_value}, points on the hull: {count_on_hull}")
print("Points on hull:", [p for p in my_points if p in hull_set])

# Draw the configuration and show the message
draw_points_and_hull(my_points, hull_part2, count_on_hull, title=f"Convex Hull with λ={lambda_value}")
