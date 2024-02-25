def add_integer(a, b=98):
  """
  Adds two integers or floats, casting them to integers if necessary.

  Args:
      a: The first number to add.
      b: The second number to add (default: 98).

  Raises:
      TypeError: If either a or b is not an integer or float.

  Returns:
      int: The sum of a and b, cast to an integer.
  """

  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("a must be an integer or float and b must be an integer or float")

  return int(a) + int(b)

# Example usage
result = add_integer(5.5, 3)
print(result)  # Output: 8

try:
  result = add_integer("hello", 3)
except TypeError as e:
  print(e)  # Output: a must be an integer or float and b must be an integer or float

