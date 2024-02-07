#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.

    Raises:
        ValueError: If n is less than or equal to 0.
    """

    if n <= 0:
        raise ValueError("n must be greater than 0")

    triangle = []
    for i in range(n):
        row = []
        # First and last element of each row is always 1
        row.append(1)
        # Middle elements are calculated using the previous row
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

