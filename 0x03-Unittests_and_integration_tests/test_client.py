#!/usr/bin/env python3
"""Test suite for client.py
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ """

    @parameterized.expand([
        ('google', {"google": True}),
        ('abc', {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, patcher):
        """tests that GithubOrgClient.org returns the correct value.
        """
        patcher.return_value.expected
        result = GithubOrgClient(org)
        self.assertEqual(result, expected)
        patcher.assert_called_once_with("https://api.github.com/orgs/" + org)
