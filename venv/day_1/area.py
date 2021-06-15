import math

# Input 4 points and turn them into 4 lists of length 2, where the first element is the x-coordinate and the second element the y-coordinate
point_one = input("Input first point like so: a, b:\n").split(", ")
point_one = [int(i) for i in point_one]
point_two = input("Input second point like so: c, d:\n").split(", ")
point_two = [int(i) for i in point_two]
point_three = input("Input third point like so: e, f:\n").split(", ")
point_three = [int(i) for i in point_three]
point_four = input("Input fourth point like so: g, h:\n").split(", ")
point_four = [int(i) for i in point_four]

# Calculations of distances between the points by the Pythagorean Theorem
d_one_two = math.sqrt(abs(point_one[0]-point_two[0])**2 + abs(point_one[1]-point_two[1])**2)
d_two_three = math.sqrt(abs(point_two[0]-point_three[0])**2 + abs(point_two[1]-point_three[1])**2)
d_three_four = math.sqrt(abs(point_three[0]-point_four[0])**2 + abs(point_three[1]-point_four[1])**2)
d_four_one = math.sqrt(abs(point_one[0]-point_four[0])**2 + abs(point_one[1]-point_four[1])**2)

# This distance divides the quadrilateral into two triangles
d_one_three = math.sqrt(abs(point_one[0]-point_three[0])**2 + abs(point_one[1]-point_three[1])**2)

# Calculation of the semiparameter of both triangles for Heron's Theorem
s_1 = (d_one_two + d_two_three + d_one_three)/2
s_2 = (d_four_one + d_three_four + d_one_three)/2

# Calculation of both areas by Heron's Theorem
area_1 = math.sqrt( s_1*(s_1-d_one_two)*(s_1-d_two_three)*(s_1-d_one_three) )
area_2 = math.sqrt( s_2*(s_2-d_four_one)*(s_2-d_three_four)*(s_2-d_one_three) )

# Calculation of entire area
area = area_1 + area_2

# Output
print(f"\nArea of quadrilateral = {area}")



