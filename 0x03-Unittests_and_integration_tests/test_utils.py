#!/usr/bin/env python3
"""Parameterize a unit test"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A unit test"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Testing for output

        Args:
            nest_map (Dict): Nested dictionary
            path: The sequence of keys to navigate through the dictionary
            expected: The expected result from the function call
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not fouund in the nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map"),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected_m):
        """Handle Error"""
        with self.assertRaises(KeyError) as em:
            access_nested_map(nested_map, path)
        self.assertEqual(str(em.exception), expected_m)


if __name__ == '__main__':
    unittest.main()
