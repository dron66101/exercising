from typing import List, Union

Number = Union[int, float]

def equilateral(sides:List[Number]) -> bool:
    """Checks if triangle is equilateral depending on its given sides"""
    isEquilater = False
    zeroChecker = 0
    prevSide = 0
    for side in sides:
        zeroChecker += side
        if prevSide == side:
            isEquilater = True
        else:
            isEquilater = False
        prevSide = side
    if not zeroChecker:
        return False
    return isEquilater


def isosceles(sides:List[Number]) -> bool:
    """Checks if triangle is isosceles depending on its given sides"""
    other_sides = list()
    another_side = 0
    sum_of_sides = 0 
    first_side = 0
    for idx, side in enumerate(sides):
        if idx > 0 and side in other_sides:
            sum_of_sides = side*2
            if first_side and sum_of_sides < first_side:
                return False
        else:
            other_sides.append(side)
            if another_side:
                first_side = another_side
            another_side = side
        
    if another_side and another_side < sum_of_sides:
        return True
    elif another_side:
        return False
    return True


def scalene(sides:List[Number]) -> bool:
    """Checks if triangle is scalene depending on its given sides"""
    other_sides = list()
    for side in sides:
        if side in other_sides:
            return False
        else:
            other_sides.append(side)
    if sum(sides[:2]) < sides[2] or sum(sides[1:]) < sides[0] or sides[0] + sides[2] < sides[1]:
        return False
    return True
