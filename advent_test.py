from advent import calculate_fuel, calculate_fuel_sum

def test_example():
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100756) == 33583

def test_fuel_sum():
    assert calculate_fuel_sum() == 3154112
