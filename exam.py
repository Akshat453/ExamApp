def calculate_marks(obtained, total):
    for value in (obtained, total):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Marks must be numbers")
    if total <= 0:
        raise ValueError("Total marks must be greater than zero")
    if obtained < 0 or obtained > total:
        raise ValueError("Obtained marks must be between 0 and total marks")
    return round(obtained / total * 100, 2)
