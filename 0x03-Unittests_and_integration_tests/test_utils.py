#!/usr/bin/env python3
"""Parameterize a unit test"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """Handle Error"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        """Creaing a mock response"""
        with patch('requests.get') as mock_get:
            mock_res = Mock()
            mock_res.json.return_value = test_payload
            mock_get.return_value = mock_res

            # Call get_json and assert the result
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

        # Assert that requests.get was called once with the url
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Parameterize and patch"""
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            instance = TestClass()
            # Call a_property twice
            first_call = instance.a_property
            second_call = instance.a_property

            # Check that the result is correct
            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)
            # Ensure a_method is called only once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
