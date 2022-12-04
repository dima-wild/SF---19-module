import pytest
from app.calculator import Calculator


class TestFunctions:
    def setup(self):
        self.calculator = Calculator

    def test_multiplication_correct(self):
        assert self.calculator.multiplication(self, 3, 3) == 9

    def test_division_correct(self):
        assert self.calculator.division(self, 12, 3) == 4

    def test_subtraction_correct(self):
        assert self.calculator.subtraction(self, 15, 8) == 7

    def test_addition_correct(self):
        assert self.calculator.addition(self, 6, 8) == 14