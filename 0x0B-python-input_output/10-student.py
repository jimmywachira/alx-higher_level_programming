#!/usr/bin/python3

"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

0x0B-python-input_output/100-append_after.py


#!/usr/bin/python3

"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
