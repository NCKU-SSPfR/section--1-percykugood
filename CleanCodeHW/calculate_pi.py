import random

# Constant settings
RADIUS = 1
NUM_POINTS = 1000000
AREA_FACTOR = 4
SQUARE_EXPONENT = 2
POINT_COUNT_INCREMENT = 1

inside_circle = 0

# Randomly generate points and count those inside the circle
for _ in range(NUM_POINTS):
    x_coordinate = random.uniform(-RADIUS, RADIUS)
    y_coordinate = random.uniform(-RADIUS, RADIUS)
    if x_coordinate**SQUARE_EXPONENT + y_coordinate**SQUARE_EXPONENT <= RADIUS**SQUARE_EXPONENT:
        inside_circle += POINT_COUNT_INCREMENT

# Estimate pi based on the number of points inside the circle
pi_neapple = (inside_circle / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {pi_neapple}")
