#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized

from utils import (access_nested_map,)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_answer: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected_answer)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)