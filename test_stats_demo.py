"""
These tests ensure the descriptive statistics functions are accurate
"""

import pytest
from stats_demo import (calculate_mean, calculate_median, calculate_mode,
                           calculate_standard_deviation, calculate_range)

def test_calculate_mean():
    """
    test that the calculate_mean function works correctly
    """
    assert calculate_mean([1, 2, 3, 4, 5]) == 3

def test_calculate_median():
    """
    test that the calculate_median function works correctly
    """
    assert calculate_median([1, 2, 3, 4, 5]) == 3
    assert calculate_median([1, 2, 3, 4, 5, 6]) == 3.5

def test_calculate_mode():
    """
    test that the calculate_mode function works correctly
    """
    assert calculate_mode([1, 2, 2, 3, 4]) == 2
    assert calculate_mode([1, 1, 2, 3, 3]) == 1

def test_calculate_standard_deviation():
    """
    test that the calculate_standard_deviation function works correctly
    """
    assert calculate_standard_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.5811, 0.0001)

def test_calculate_range():
    """
    test that the calculate_range function works correctly
    """
    assert calculate_range([1, 2, 3, 4, 5]) == 4
