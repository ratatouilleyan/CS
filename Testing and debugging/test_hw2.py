import pytest
from hw2 import find_grade

students = ['Alissa', 'Ben', 'Charlie', 'Diana']
grades = ['B', 'D', 'B', 'A']

# pytest way to list used parameters to test function
@pytest.mark.parametrize('name, expected', [
    ('Charlie','B'), # typical, middle-B
    ('Alissa', 'B'), # first element
    ('Diana', 'A'), # last element
    ('Joe', None), # not found
])

def test_find_grade(name, expected): # test function
    assert find_grade(name, students, grades) == expected # match against expected