import area_rectangle


def test_integration():
    # Test case 1: Square (length = width)
    assert area_rectangle.calculate_rectangle_area(5, 5) == 25

    # Test case 2: Rectangle (length > width)
    assert area_rectangle.calculate_rectangle_area(8, 4) == 32

    # Test case 3: Rectangle (length < width)
    assert area_rectangle.calculate_rectangle_area(3, 7) != 21
