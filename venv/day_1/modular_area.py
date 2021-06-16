import math

def input_points(n):
    result = []
    for i in range(n):
        result.append(input("Input point like so: a,  b:\n").split(", "))
    return [list( map(int,i) ) for i in result]

def calculate_distance_between_points(p1, p2):
    return math.sqrt(abs(p1[0] - p2[0])**2 + abs(p1[1] - p2[1])**2)

def calculate_semiparameter(a, b, c):
    return (a+b+c)/2

def calculate_area_triangle(a, b, c):
    s = calculate_semiparameter(a, b, c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

# Input 4 points and turn them into 4 lists of length 2, where the first element is the x-coordinate and the second element the y-coordinate
points = input_points(4)

# Calculations of distances between the points by the Pythagorean Theorem
distances = []
for i in range(3):
    distances.append(calculate_distance_between_points(points[i], points[i+1]))
distances.append(calculate_distance_between_points(points[3], points[0]))
distances.append(calculate_distance_between_points(points[0], points[2]))

# Calculation of both areas by Heron's Theorem
area_1 = calculate_area_triangle(distances[0], distances[1], distances[4])
area_2 = calculate_area_triangle(distances[2], distances[3], distances[4])

area = round(area_1 + area_2, 10)

print(f"Area: {area}")
