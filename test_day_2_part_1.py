import pytest
from day_2_part_1 import intcode
def test_intcode():
    program = [1,0,0,0,99]
    result = intcode(program)
    assert result == [2,0,0,0,99]

    program = [2,3,0,3,99]
    result = intcode(program)
    assert result == [2,3,0,6,99]

    program = [2,4,4,5,99,0]
    result = intcode(program)
    assert result == [2,4,4,5,99,9801]

    program = [1,1,1,4,99,5,6,0,99]
    result = intcode(program)
    assert result == [30,1,1,4,2,5,6,0,99]

