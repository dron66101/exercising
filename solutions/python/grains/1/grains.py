def square(number: int) -> int:
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return pow(2, number-1)

 
def total() -> int:
    total_grains_number = 0
    for number in range(1, 65):
        total_grains_number += square(number)
    return total_grains_number