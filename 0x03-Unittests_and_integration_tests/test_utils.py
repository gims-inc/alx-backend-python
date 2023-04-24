#!/usr/bin/env python3
"""Test Suite for utils.py
"""
from utils import access_nested_map, get_json
import unittest
from unittest.mock import patch, Mock
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


class TestGetJson(unittest.TestCase):
    """Class for testing get_json method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self, turl, expected_json, mock_requests):
        """Test output  of get_json against payload
        and test whether mocked get method was called once
        (per input) with test_url as an argv
        """
        mock_resp = Mock()
        mock_resp.json.return_value = expected_json
        mock_resp.get.return_value = mock_resp
        result = get_json(turl)
        self.assertEqual(result, expected_json)
