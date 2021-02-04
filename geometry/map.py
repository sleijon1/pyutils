def adjacent_tiles(grid: list, coord: tuple, wrap=False) -> list:
    """
    Returns the elements that are adjacent to
    position coord (x, y)

    Keyword args:
    grid -- represented as a nested list
    coord -- of element whos adjacents we are seeking
    wrap -- if we want to wrap around the grid edges
    """
    x, y = coord
    adjacent = []
    if wrap:
        # TODO implement
        pass
    else:
        try:
            # below
            adjacent.append(grid[y+1][x])
            # below right
            adjacent.append(grid[y+1][x+1])
        except IndexError:
            pass
        try:
            # right
            adjacent.append(grid[y][x+1])
        except IndexError:
            pass

        if y > 0:
            # above
            adjacent.append(grid[y-1][x])
            if x < len(grid[0])-1:
                # above right
                adjacent.append(grid[y-1][x+1])
            if x > 0:
                # above left
                adjacent.append(grid[y-1][x-1])
        if x > 0:
            # left
            adjacent.append(grid[y][x-1])
            if y < len(grid)-1:
                # below left
                adjacent.append(grid[y+1][x-1])
    return adjacent
