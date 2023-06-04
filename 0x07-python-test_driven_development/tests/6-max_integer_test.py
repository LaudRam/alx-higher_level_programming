#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' Defines unittests for max_integer([..]) '''
    def test_none(self):
        ''' Tests for parameter 'None' being passed '''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        ''' Tests an empty list '''
        self.assertIsNone(max_integer([]))

    def test_no_param(self):
        ''' Tests for no parameter '''
        self.assertIsNone(max_integer())

    def test_all_equal(self):
        ''' Tests when values are the same '''
        self.assertEqual(max_integer([6, 6, 6, 6]), 6)

    def test_strings(self):
        ''' Tests for string values in the list '''
        with self.assertRaises(TypeError):
            max_integer([3, 'Test', 2, 1])

    def test_negatives(self):
        ''' Tests for negative values '''
        self.assertEqual(max_integer([-1, -69, -420, -2]), -69)

    def test_floats(self):
        ''' Tests for floating point numbers '''
        self.assertEqual(max_integer([4.544, -9.8, 8.3, 3.3333]), 8.3)

    def test_one(self):
        ''' Tests for list with only one parameter '''
        self.assertEqual(max_integer([13]), 13)

    def test_beginning(self):
        ''' Tests for when max value is at the beginning '''
        self.assertEqual(max_integer([80, 6, 6, 6]), 80)

    def test_ordered(self):
        ''' Tests for ordered list of integers '''
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)

    def test_unordered(self):
        ''' Tests for unordered list of integers '''
        self.assertEqual(max_integer([6, 8, 2, 4]), 8)

    def test_correct(self):
        ''' Tests for passing an argument that's expected to succeed '''
        self.assertEqual(max_integer([1, 6, 100, 4, 0, -1, 10]), 100)
