import src.day_2.modular_area as area

def test_calculate_distance_between_points():
    assert area.calculate_distance_between_points([0, 0], [3, 4]) == 5

def test_calculate_semiparameter():
    assert area.calculate_semiparameter(1, 2 , 3) == 3

def test_calculate_area_triangle():
    assert area.calculate_area_triangle(3, 4, 5) == 6

def test_calculate_area_quadrilateral():
    assert area.calculate_area_quadrilateral([[-1, 1], [-1, -1], [1, -1], [1, 1]]) == 4