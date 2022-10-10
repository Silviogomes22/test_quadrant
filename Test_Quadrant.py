from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_quadrant_coordinate_first():
    # Arrange / Setup
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"

def test_should_get_quadrant_coordinate_second():
    a = -10
    b = 5
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)
    result = quadrant.get_quadrant_coordinate()

    assert result == "Second"

def test_should_get_quadrant_coordinate_third():
    a = -5
    b = -5
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)
    result = quadrant.get_quadrant_coordinate()
    assert result == "Third"

def test_should_get_quadrant_coordinate_fourth():

    a = 5
    b = -1
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)
    result = quadrant.get_quadrant_coordinate()
    assert result == "Fourth"