from main import *


def test_open ():
    assert open_cost() == [150, 1200, 300, 500, 829, 2750]

def test_total():
    assert tax(open_cost()) == 6361.0

def main_test():
    assert terminal() is None
