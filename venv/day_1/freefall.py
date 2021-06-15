import math

height = float(input("Input height here:\n"))
g = 9.81
time_in_s = math.sqrt(2*height/g)
print(f"Time of free fall: {time_in_s}")
