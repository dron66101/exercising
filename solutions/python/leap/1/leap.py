def leap_year(year:int) -> bool:
    """
    param:int - year, the year to test
    return:bool - function returns bool whether year is leap or not
    """
    return True if not year % 4 and (False if not year % 100 and year % 400 else True) else False
