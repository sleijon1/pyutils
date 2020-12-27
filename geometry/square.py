def rotations_flips(square: list):
    """ Returns all rotations and mirrorings of a square
    Keyword args:
    square -- list representing a square
    """
    permutations = []
    permutations.append(list(square))
    permutations.append(rotate_90(list(square)))
    permutations.append(rotate_90(rotate_90(list(square))))
    permutations.append(rotate_90(rotate_90(rotate_90(list(square)))))
    permutations.append(reflect_x(rotate_90(list(square))))
    permutations.append(reflect_y(rotate_90(list(square))))
    permutations.append(reflect_x(list(square)))
    permutations.append(reflect_y(list(square)))
    return permutations


def reflect_x(square: list) -> [str]:
    """ reflects square around the x-axis
    Keyword args:
    square -- list representing a square
    """
    list.reverse(square)
    return square


def reflect_y(square: list) -> [str]:
    """ reflects square around the y-axis
    Keyword args:
    square -- list representing a square
    """
    for i, row in enumerate(square):
        square[i] = row[::-1]
    return square


def rotate_90(square: list):
    """ rotates square 90 degrees
    Keyword args:
    square -- list representing a square
    """
    rows = ['' for _ in range(len(square[0]))]
    for i, row in enumerate(square[::-1]):
        for j, el in enumerate(row):
            rows[j] += el
    return rows
