#!/usr/bin/env python3
"""Test Suite for utils.py
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing Nested Map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """Test for expected output"""
        result = access_nested_map(map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, map, path):
        """Test exceptions --KeyError"""
        with self.assertRaises(Exception):
            access_nested_map(map, path)
