{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

def minimum(value1, value2, value3, value4):
    """Return the minimum of four values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    if value4 < min_value:
        min_value = value4
    return min_value

print(f'The maximum value is', maximum(12, 27, 36))
print(f'The minimum value is', minimum(15, 9, 27, 14))
print(f'My name is Kim Leach')