#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """multiplies two matrices

    Args:
    m_a [list]: first matrix
    m_b [list]: second matrix

    Raises:
    TypeError: m_a must be a list or m_b must be a list
    TypeError: m_a must be a list of lists or m_b must be a list of lists
    TypeError: m_a should contain only integers or floats
    or m_b should contain only integers or floats
    TypeError: each row of m_a must should be of the same size
    or each row of m_b must should be of the same size
    ValueError: m_a and m_b can't be multiplied

    Returns: the result
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not any(isinstance(y, list) for y in m_a):
        raise TypeError("m_a must be a list of lists")
    if not any(isinstance(y, list) for y in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(x, (float, int))for y in m_a for x in y):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (float, int))for y in m_b for x in y):
        raise TypeError("m_b should contain only integers or floats")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(len(x) == len(next(iter(m_a))) for x in iter(m_a)):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(x) == len(next(iter(m_b))) for x in iter(m_b)):
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[sum(a * b for a, b in zip(a_row, b_col)) for b_col in zip(*m_b)]
            for a_row in m_a]
