import math

point_one = input("Input first point like so: a, b:\n").split(", ")
point_one = [int(i) for i in point_one]
point_two = input("Input second point like so: a, b:\n").split(", ")
point_two = [int(i) for i in point_two]
point_three = input("Input third point like so: a, b:\n").split(", ")
point_three = [int(i) for i in point_three]
point_four = input("Input fourth point like so: a, b:\n").split(", ")
point_four = [int(i) for i in point_four]

d_one_two = math.sqrt(abs(point_one[0]-point_two[0])**2 + abs(point_one[1]-point_two[1])**2)
d_two_three = math.sqrt(abs(point_two[0]-point_three[0])**2 + abs(point_two[1]-point_three[1])**2)
d_three_four = math.sqrt(abs(point_three[0]-point_four[0])**2 + abs(point_three[1]-point_four[1])**2)
d_four_one = math.sqrt(abs(point_one[0]-point_four[0])**2 + abs(point_one[1]-point_four[1])**2)




